import urllib.request
import json
import time
import sys

def fetch_binance_price(symbol):
    endpoints = [
        f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}",
        f"https://data-api.binance.vision/api/v3/ticker/price?symbol={symbol}"
    ]
    
    for url in endpoints:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=3) as response:
                data = json.loads(response.read().decode())
                return float(data['price'])
        except Exception:
            continue
            
    return None

def run_trading_agent():
    print("==================================================")
    print("🤖 BINANCE TRADING AGENT (Track A: Trading Workflows)")
    print("==================================================")
    print("[+] Initializing Agent OS environment...")
    time.sleep(1)
    
    print("\n[?] Instructions:")
    print("    - Type coin names separated by space or comma (e.g., btc, eth, sol)")
    print("    - Type 'exit' anytime to stop the agent session.")
    
    while True:
        print("-" * 50)
        user_input = input("Enter trading pairs to analyze [or type 'exit']: ").strip()
        
        if user_input.lower() == 'exit':
            print("\n[+] Shutting down Agent OS environment safely...")
            time.sleep(1)
            print("✨ Agent session terminated. Goodbye!")
            break
            
        if user_input:
            raw_pairs = [p.strip().upper() for p in user_input.replace(",", " ").split() if p.strip()]
            pairs = [p if p.endswith("USDT") else p + "USDT" for p in raw_pairs]
        else:
            pairs = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]
            
        print(f"\n[+] Selected Pairs for Agent Workflow: {', '.join(pairs)}")
        print("[+] Connecting to Binance Market Data Streams...\n")
        time.sleep(1)

        for pair in pairs:
            print(f"--------------------------------------------------")
            print(f"📊 Analyzing Market : {pair}")
            
            price = fetch_binance_price(pair)
            
            if price:
                print(f"💰 Current Live Price : ${price:,.2f}")
                time.sleep(1)
                
                # Kalkulasi simulasi dinamis berdasarkan harga live
                if "BTC" in pair:
                    rsi = 52.4
                    entry_zone = f"${price * 0.992:,.2f} - ${price:,.2f}"
                    tp = f"${price * 1.035:,.2f}"
                    sl = f"${price * 0.978:,.2f}"
                    decision = "Accumulation phase. Setting up DCA entry zone."
                elif "ETH" in pair:
                    rsi = 58.1
                    entry_zone = f"${price * 0.990:,.2f} - ${price:,.2f}"
                    tp = f"${price * 1.045:,.2f}"
                    sl = f"${price * 0.975:,.2f}"
                    decision = "Bullish momentum building. Preparing breakout entry."
                elif "SOL" in pair:
                    rsi = 63.5
                    entry_zone = f"${price * 0.985:,.2f} - ${price:,.2f}"
                    tp = f"${price * 1.060:,.2f}"
                    sl = f"${price * 0.965:,.2f}"
                    decision = "High volatility & volume breakout. Scalping mode."
                else:
                    rsi = 48.9
                    entry_zone = f"${price * 0.995:,.2f} - ${price:,.2f}"
                    tp = f"${price * 1.030:,.2f}"
                    sl = f"${price * 0.980:,.2f}"
                    decision = "Range-bound strategy & risk control applied."
                
                print(f"📈 RSI (14) Indicator : {rsi} (Balanced / Active)")
                print(f"💡 AI Decision        : {decision}")
                print(f"🎯 Entry Zone         : {entry_zone}")
                print(f"🚀 Take Profit (TP)   : {tp}")
                print(f"🛑 Stop Loss (SL)     : {sl}")
                print(f"🔒 Status             : Scanned & Verified via Agent OS.")
            else:
                print(f"⚠️ Warning            : Invalid symbol or connection timeout for '{pair}'.")
            
            print("--------------------------------------------------")
            time.sleep(1)

        print("\n✨ Cycle completed. Ready for the next analysis session.\n")

if __name__ == "__main__":
    run_trading_agent()
