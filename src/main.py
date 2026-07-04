# src/main.py
import sys
from src.utils.logger import setup_logger
from src.agents.PredictionMarketAgent import PredictionMarketAgent
from src.agents.DataScraperAgent import DataScraperAgent
from src.agents.ModelInferenceAgent import ModelInferenceAgent
from src.agents.RiskManagerAgent import RiskManagerAgent

logger = setup_logger("CoreOrchestrationLoop")

def run_arbitrage_pipeline(asset: str):
    logger.info(f"==== STARTING MULTI-AGENT EXECUTION CYCLE FOR {asset.upper()} ====")
    
    # 1. Initialize core system modules
    market_agent = PredictionMarketAgent()
    scraper_agent = DataScraperAgent()
    kronos_agent = ModelInferenceAgent()
    risk_agent = RiskManagerAgent(fractional_multiplier=0.5)
    
    # 2. Phase 1: Retrieve pricing across parallel global prediction markets
    market_data = market_agent.fetch_market_predictions(asset)
    
    # 3. Phase 2: Retrieve high density historical timeseries via Apify
    historical_df = scraper_agent.fetch_historical_bars(asset, limit=1000)
    
    # 4. Phase 3: Structural time series inference via Kronos Model logic
    prediction = kronos_agent.predict_next_move(historical_df)
    
    # 5. Phase 4: Risk Sizing and Arbitrage Execution Optimization Logic
    polymarket_implied = market_data["polymarket"]["implied_probability"]
    kalshi_implied = market_data["kalshi"]["implied_probability"]
    
    # Check for internal structural arbitrage across intervals (Scale Idea!)
    arbitrage_spread = abs(polymarket_implied - kalshi_implied)
    logger.info(f"Inter-market structural spread observed: {arbitrage_spread:.4f}")
    
    # Position sizing optimized using Kronos directional probabilities against specific market metrics
    poly_allocation = risk_agent.calculate_allocation(prediction["probability_up"], polymarket_implied)
    kalshi_allocation = risk_agent.calculate_allocation(prediction["probability_up"], kalshi_implied)
    
    # 6. Hermes Feedback / Evaluation loop block logs summary results cleanly
    logger.info("==== SYSTEM PIPELINE SUMMARY SUMMARY ====")
    logger.info(f"Asset Target:       {asset.upper()}")
    logger.info(f"Kronos Prediction:  {prediction['predicted_direction']} (p={prediction['probability_up']})")
    logger.info(f"Polymarket Sizing:  {poly_allocation * 100}% Portfolio Capital")
    logger.info(f"Kalshi Sizing:      {kalshi_allocation * 100}% Portfolio Capital")
    
    if arbitrage_spread > 0.02:
        logger.info(f"🔥 ARBITRAGE SIGNAL ACTIVE: Mispricing detected between platforms of {arbitrage_spread*100:.1f}%.")
        
    logger.info("==== AGENT LOOP RE-EVALUATION CYCLE WAITING FOR NEXT BAR ====\n")

if __name__ == "__main__":
    # Run the continuous sequence loop for major assets specified inside project parameters
    targets = ["btc", "eth"]
    for crypto in targets:
        try:
            run_arbitrage_pipeline(crypto)
        except Exception as main_err:
            logger.critical(f"Pipeline crashed during execution for asset {crypto}: {str(main_err)}")