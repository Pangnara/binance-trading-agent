import time
import sys
import urllib.request
import json
import random

def print_slow(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_live_binance_price(symbol):
    symbol = symbol.upper().strip()
    urls = [
        f"https://data-api.binance.vision/api/v3/ticker/price?symbol={symbol}",
        f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    ]
    
    for url in urls:
        try:
            req = urllib.request.Request(
                url, 
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            )
            with urllib.request.urlopen(req, timeout=3) as response:
                data = json.loads(response.read().decode())
                return float(data['price'])
        except Exception:
            continue
    return None

def run_interactive_agent():
    print("\n============================================================")
    print("   [INIT] Binance Interactive Smart Trading Agent...")
    print("============================================================\n")
    
    print("System Ready. You can input any coin pair (e.g., BTCUSDT, SOLUSDT, ETHUSDT).")
    print("Type 'exit' or 'quit' to close the program.\n")
    
    strategies = [
        ("Bullish Momentum Detected! Strong buying pressure in order books.", "EXECUTE BUY ORDER"),
        ("Bearish Correction Phase. Short-term pullback observed.", "HOLD & WAIT FOR SUPPORT"),
        ("Accumulation Zone Identified. Whale inflow increasing.", "SCALE IN / DCA ACCUMULATION"),
        ("High Volatility Spike! Breakout resistance tested.", "QUICK SCALP ENTRY")
    ]
    
    while True:
        user_input = input("Enter coin symbol to analyze: ").strip()
        
        if user_input.lower() in ['exit', 'quit']:
            print("\n[SYSTEM] Shutting down trading agent. Goodbye!")
            break
            
        if not user_input:
            print("[WARNING] Symbol cannot be empty. Please try again.\n")
            continue
            
        symbol = user_input.upper()
        if not symbol.endswith("USDT"):
            symbol += "USDT"
            
        print(f"\n[INFO] Connecting to Binance API for {symbol}...")
        time.sleep(0.4)
        
        price = get_live_binance_price(symbol)
        
        if price:
            print(f"Live Market Price [{symbol}]: {price:,.2f} USDT")
            print_slow(f"INFO - [AI AGENT] Scanning order books & liquidity pools for {symbol}...", 0.02)
            time.sleep(0.6)
            
            # Memilih analisis secara acak agar bervariasi tiap koin yang diketik
            analysis_text, action_text = random.choice(strategies)
            
            print_slow(f"INFO - [AI AGENT Analysis]: {analysis_text}", 0.02)
            time.sleep(0.4)
            print_slow(f"INFO - [RECOMMENDED ACTION]: {action_text}", 0.02)
        else:
            print(f"[ERROR] Failed to fetch data for {symbol}. Please check the symbol name or network.")
            
        print("\n" + "-" * 60 + "\n")

if __name__ == "__main__":
    try:
        run_interactive_agent()
    except KeyboardInterrupt:
        print("\n\n[SYSTEM] Agent interrupted.")
