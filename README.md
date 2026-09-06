# 🤖 Binance Trading Agent (Trading Workflows)

An autonomous AI trading agent built for the Binance Agent OS ecosystem. This repository demonstrates a robust, interactive trading workflow that connects to real-time market data streams, evaluates technical indicators (RSI), and provides precise risk management levels (Entry, Take Profit, Stop Loss).

---

## 🌟 Key Features

* Live Market Data Integration: Fetches real-time cryptocurrency ticker prices directly from Binance Public APIs with an automatic fallback mechanism (binance.vision) for high availability.
* Interactive CLI Interface: Allows users to dynamically input custom trading pairs (e.g., BTC, ETH, SOL) or use intelligent defaults.
* Continuous Monitoring Loop: Features an active session loop so the agent stays online, allowing multi-session analysis and a clean exit command (exit).
* Advanced AI Decision & Risk Metrics: Automatically calculates and displays technical checks (RSI), AI decisions, optimal entry zones, Take Profit (TP), and Stop Loss (SL) targets based on live prices.
* Agent OS Compliance: Fully integrated with standard agent manifests (agent-manifest.json) tailored for Track A submission.

---

## 📂 Repository Structure

```text
binance-trading-agent/
├── agent-manifest.json    # Agent OS registration and metadata
├── main.py                # Core agent logic, interactive loop, and live API fetcher
└── README.md              # Project documentation
```
## 🚀 Quick Start Guide

### Prerequisites
* Python 3.x installed on your system.
* No external libraries required (uses Python standard libraries: urllib, json, time, sys).

### Running the Agent
1. Clone the repository or download the source code.
   ```bash
   git clone https://github.com/Pangnara/binance-trading-agent.git
   ```
3. Open your terminal in the project directory.
4. Run the main agent script:
   ```bash
   python main.py
   ```
5. Enter your desired coin symbols (e.g.,btc,bnb,eth) or press Enter to use default pairs.
6. Type exit whenever you want to safely terminate the agent session.
   
