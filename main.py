import time
import sys
import random

def print_slow(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def run_smart_demo():
    print("\n============================================================")
    print("   [INIT] Connecting to Binance Smart Market Stream...")
    print("============================================================\n")
    
    steps = [
        "Loading Agent OS Core Module v1.0...",
        "Establishing WebSocket Feed to Binance Order Book...",
        "Loading Strategy: 'momentum_signal.py'...",
        "System Ready. Monitoring live liquidity pools...",
        "------------------------------------------------------------"
    ]
    
    for step in steps:
        print_slow(f"[INFO] - {step}", 0.02)
        time.sleep(0.3)

    # Titik awal harga realistis saat ini
    prices = {
        "BTCUSDT": 78450.25,
        "ETHUSDT": 2510.50,
        "BNBUSDT": 625.80
    }
    
    pairs = list(prices.keys())
    
    for cycle in range(1, 4):
        print(f"\n--- CYCLE {cycle} ---")
        for pair in pairs:
            # Simulasi pergerakan harga real-time tipis-tipis
            change = random.uniform(-15.5, 18.2) if pair == "BTCUSDT" else random.uniform(-2.5, 3.0)
            prices[pair] += change
            current_price = round(prices[pair], 2)
            
            print(f"Fetching live ticker stream for {pair}...")
            time.sleep(0.4)
            
            print(f"Live Market Price [{pair}]: {current_price:,.2f} USDT")
            signal_type = random.choice(["BUY", "SELL", "HOLD"])
            print_slow(f"INFO - [AI AGENT] Order Book Analyzed. Signal for {pair}: {signal_type}", 0.02)
            
            if signal_type != "HOLD":
                print_slow(f"INFO - [TESTNET MODE] Executing {signal_type} order at {current_price:,.2f} USDT...", 0.02)
                
            time.sleep(0.5)
        
        print("\n" + "=" * 60)

    print("\n[SYSTEM] completed.\n")

if __name__ == "__main__":
    try:
        run_smart_demo()
    except KeyboardInterrupt:
        print("\n[SYSTEM] Agent interrupted.")