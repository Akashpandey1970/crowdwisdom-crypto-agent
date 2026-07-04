# crowdwisdom-crypto-agent

> Multi-agent crypto prediction and arbitrage platform using Hermes and Kronos.

![GitHub stars](https://img.shields.io/github/stars/Akashpandey1970/crowdwisdom-crypto-agent?style=for-the-badge&logo=github) ![GitHub forks](https://img.shields.io/github/forks/Akashpandey1970/crowdwisdom-crypto-agent?style=for-the-badge&logo=github) ![GitHub issues](https://img.shields.io/github/issues/Akashpandey1970/crowdwisdom-crypto-agent?style=for-the-badge&logo=github) ![Last commit](https://img.shields.io/github/last-commit/Akashpandey1970/crowdwisdom-crypto-agent?style=for-the-badge&logo=github) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

## 📑 Table of Contents

- [Description](#description)
- [Key Features](#key-features)
- [Use Cases](#use-cases)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Development Setup](#development-setup)
- [Contributors](#contributors)
- [Contributing](#contributing)
- [License](#license)

## 📝 Description

crowdwisdom-crypto-agent is a production-grade multi-agent platform designed for automated crypto prediction and arbitrage. Built on the Hermes Agent framework, the system is designed to forecast short-term trends for major digital assets and programmatically allocate capital across popular prediction markets. It addresses the complexity of cross-market execution and mathematical position sizing by distributing tasks to specialized agents.

## ✨ Key Features

- **🔄 Multi-Agent Orchestration Loop** — Coordinates specialized agents including PredictionMarketAgent, DataScraperAgent, and ModelInferenceAgent to execute end-to-end arbitrage cycles.
- **📈 Kronos Time-Series Forecasting** — Utilizes the Kronos Time-Series Foundation Model to predict 5-minute close trends on BTC and ETH.
- **⚖️ Prediction Market Arbitrage** — Identifies spreads and manages automated position allocations across Polymarket and Kalshi platforms.
- **🛡️ Fractional Kelly Risk Management** — Calculates risk-adjusted position sizing using a RiskManagerAgent configured with a 0.5 fractional Kelly Criterion multiplier.
- **🕸️ Apify-Sourced Data Scraping** — Programmatically retrieves pricing data across parallel global markets using a dedicated scraping agent.

## 🎯 Use Cases

- Automating 5-minute close trend predictions for BTC and ETH using a time-series foundation model.
- Executing automated arbitrage strategies based on price spreads between Polymarket and Kalshi.
- Deploying a modular, multi-agent pipeline to safely size market positions using the fractional Kelly Criterion.

## 🛠️ Tech Stack

- 🐍 **Python**

## ⚡ Quick Start

```bash

# 1. Clone the repository
git clone https://github.com/Akashpandey1970/crowdwisdom-crypto-agent.git

# 2. Create & activate a virtualenv
python -m venv venv && source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

## 📁 Project Structure

```
.
├── LICENSE
├── pyproject.toml
└── src
    ├── __init__.py
    ├── agents
    │   ├── DataScraperAgent.py
    │   ├── ModelInferenceAgent.py
    │   ├── PredictionMarketAgent.py
    │   ├── RiskManagerAgent.py
    │   └── __init__.py
    ├── config.py
    ├── crowdwisdom_crypto_agent.egg-info
    │   ├── PKG-INFO
    │   ├── SOURCES.txt
    │   ├── dependency_links.txt
    │   ├── requires.txt
    │   └── top_level.txt
    ├── dashboard.py
    ├── main.py
    └── utils
        ├── __init__.py
        └── logger.py
```

## 🛠️ Development Setup

### Python
1. Install Python (v3.10+ recommended)
2. `python -m venv venv && source venv/bin/activate`  (Windows: `venv\Scripts\activate`)
3. `pip install -r requirements.txt`

## 👥 Contributors

Thanks to everyone who has contributed to this project:

<p align="left">
<a href="https://github.com/Akashpandey1970" title="Akashpandey1970"><img src="https://avatars.githubusercontent.com/u/185476628?v=4&s=64" width="64" height="64" alt="Akashpandey1970" style="border-radius:50%" /></a>
</p>

[See the full list of contributors →](https://github.com/Akashpandey1970/crowdwisdom-crypto-agent/graphs/contributors)

## 👥 Contributing

Contributions are welcome! Here's the standard flow:

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/Akashpandey1970/crowdwisdom-crypto-agent.git`
3. **Branch**: `git checkout -b feature/your-feature`
4. **Commit**: `git commit -m 'feat: add some feature'`
5. **Push**: `git push origin feature/your-feature`
6. **Open** a pull request

Please follow the existing code style and include tests for new behavior where applicable.

## 📜 License

This project is licensed under the **MIT** License.
