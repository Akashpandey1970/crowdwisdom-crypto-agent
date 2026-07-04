import sys
import os
import time

# Absolute Path Injection Guardrail to prevent ModuleNotFoundError
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd
import numpy as np
from src.agents.PredictionMarketAgent import PredictionMarketAgent
from src.agents.DataScraperAgent import DataScraperAgent
from src.agents.ModelInferenceAgent import ModelInferenceAgent
from src.agents.RiskManagerAgent import RiskManagerAgent

# Theme & Header Layout Config
st.set_page_config(
    page_title="CrowdWisdom Alpha Stream", 
    page_icon="🦅", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom dark-theme card styling inject
st.markdown("""
    <style>
    .metric-card {
        background-color: #1e293b;
        border-radius: 8px;
        padding: 15px;
        border: 1px solid #334155;
    }
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- SESSION STATE STATE SEEDING -----------------
# We seed price history to ensure the chart starts with realistic historical context
if "price_history" not in st.session_state:
    st.session_state.price_history = {
        "BTC": list(np.random.normal(65000, 150, 100)),
        "ETH": list(np.random.normal(3500, 15, 100))
    }

# Sidebar Controls
st.sidebar.title("🎮 Telemetry Controls")
asset = st.sidebar.selectbox("Active Asset Asset Layer", ["BTC", "ETH"])
fractional_multiplier = st.sidebar.slider("Kelly Fractional Safety Multiplier", 0.1, 1.0, 0.5, step=0.05)
tick_interval = st.sidebar.slider("Simulation Live Update Speed (s)", 1, 5, 2)
st.sidebar.markdown("---")
is_live = st.sidebar.toggle("🟢 Activate Live Trading Feed", value=True)

# Instantiate Core System Agents
markets_agent = PredictionMarketAgent()
scraper_agent = DataScraperAgent()
kronos_agent = ModelInferenceAgent()
risk_agent = RiskManagerAgent(fractional_multiplier=fractional_multiplier)

st.title("🦅 CrowdWisdom Live Arbitrage Monitor")
st.markdown("Automated cross-market pricing parity scanner matching Polymarket, Kalshi, and Kronos models.")

# Main dynamic layout container placeholders
alert_placeholder = st.empty()
metrics_row = st.columns(4)
chart_placeholder = st.empty()
position_placeholder = st.empty()

# ----------------- RUNTIME STREAMING LOOP -----------------
# Using a continuous loop to stream ticks live onto the chart
while True:
    # 1. Update Asset Price Metrics
    prices_list = st.session_state.price_history[asset]
    last_price = prices_list[-1]
    
    # Calculate a simulated price drift
    drift = np.random.normal(0, last_price * 0.001)
    new_price = round(last_price + drift, 2)
    prices_list.append(new_price)
    
    # Keep historical window bounded at 150 records to save memory
    if len(prices_list) > 150:
        prices_list.pop(0)
    st.session_state.price_history[asset] = prices_list

    # Assemble structured DataFrame to feed into Kronos Transformer Agent
    mock_df = pd.DataFrame({
        "open": [p * 0.999 for p in prices_list],
        "high": [p * 1.001 for p in prices_list],
        "low": [p * 0.998 for p in prices_list],
        "close": prices_list,
        "volume": [np.random.uniform(10, 100) for _ in prices_list]
    })

    # 2. Invoke Multi-Agent Reasoning Chains
    prediction = kronos_agent.predict_next_move(mock_df)
    market_metrics = markets_agent.fetch_market_predictions(asset)
    
    # Fetch price points from prediction markets
    poly_p = market_metrics["polymarket"]["implied_probability"]
    kalshi_p = market_metrics["kalshi"]["implied_probability"]
    arbitrage_spread = abs(poly_p - kalshi_p)

    # 3. Size positions based on updated Risk Limits
    poly_allocation = risk_agent.calculate_allocation(prediction["probability_up"], poly_p)
    kalshi_allocation = risk_agent.calculate_allocation(prediction["probability_up"], kalshi_p)

    # 4. Render Dynamic Alerts
    with alert_placeholder:
        if arbitrage_spread > 0.02:
            st.error(f"🔥 ACTIVE ARBITRAGE SIGNAL: Inter-market pricing divergence detected! Spread is {arbitrage_spread * 100:.2f}%")
        else:
            st.success("🎯 Market Spreads Balanced. Automated pipelines scouring order-books...")

    # 5. Render Metric Overviews
    with metrics_row[0]:
        st.metric(
            label="Live Index Reference", 
            value=f"${new_price:,.2f}", 
            delta=f"{drift:,.2f} USD"
        )
    with metrics_row[1]:
        st.metric(
            label="Kronos Trend Prediction", 
            value=prediction["predicted_direction"], 
            delta=f"p={prediction['probability_up']:.2f} confidence"
        )
    with metrics_row[2]:
        st.metric(
            label="Polymarket Book Implied", 
            value=f"${poly_p:.2f}", 
            delta=f"Spread: {abs(new_price/100000 - poly_p):.4f}"
        )
    with metrics_row[3]:
        st.metric(
            label="Kalshi Book Implied", 
            value=f"${kalshi_p:.2f}", 
            delta=f"Spread: {abs(new_price/100000 - kalshi_p):.4f}"
        )

    # 6. Render Dynamic Line Charts
    with chart_placeholder:
        st.subheader(f"📊 Programmatic Live Feed Array ({asset}/USDT)")
        display_df = pd.DataFrame({
            "Market Price": prices_list
        })
        st.line_chart(display_df, use_container_width=True)

    # 7. Render Position Allocation Metrics
    with position_placeholder:
        st.subheader("💼 Active Sizing (Fractional-Kelly Rules)")
        c1, c2 = st.columns(2)
        with c1:
            st.write(f"Polymarket Sizing Allocation: **{poly_allocation * 100:.2f}%**")
            st.progress(min(max(float(poly_allocation), 0.0), 1.0))
        with c2:
            st.write(f"Kalshi Sizing Allocation: **{kalshi_allocation * 100:.2f}%**")
            st.progress(min(max(float(kalshi_allocation), 0.0), 1.0))

    # Break loop immediately if the user turns off the Live Feed switch in the sidebar
    if not is_live:
        st.warning("⚠️ Live Telemetry Feed Stopped. Tick rendering frozen.")
        break

    time.sleep(tick_interval)