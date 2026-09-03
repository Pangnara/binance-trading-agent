import time
import requests

def get_binance_market_data(symbol):
    # Fallback URLs: api.binance.com and data-api.binance.vision
    urls = [
        f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol.upper()}USDT",
        f"https://data-api.binance.vision/api/v3/ticker/24hr?symbol={symbol.upper()}USDT"
    ]
    
    for url in urls:
        try:
            response = requests.get(url, timeout=4)
            if response.status_code == 200:
                data = response.json()
                if 'lastPrice' in data:
                    return {
                        'price': float(data['lastPrice']),
                        'price_change_percent': float(data['priceChangePercent']),
                        'high': float(data['highPrice']),
                        'low': float(data['lowPrice'])
                    }
        except Exception:
            continue
            
    return None

def main():
    print("==================================================")
    print("   BINANCE AI TRADING AGENT (WITH RISK MGMT)      ")
    print("==================================================")
    
    # Loop utama agar agen bisa dipakai terus-menerus
    while True:
        coin = input("\nEnter the coin to analyze (e.g., BTC, ETH, SOL) or type 'EXIT' to quit: ").strip().upper()
        
        if coin == 'EXIT':
            print("Thank you for using Binance AI Trading Agent. Goodbye!")
            break
            
        if not coin:
            continue
            
        symbol_check = f"{coin}USDT"
        
        print(f"\n🔍 Connecting to Binance API for {symbol_check}...")
        market_data = get_binance_market_data(coin)
        
        if market_data is None:
            print(f"❌ Asset {symbol_check} not found or connection failed on all endpoints! Please try again.")
            continue

        current_price = market_data['price']
        change_pct = market_data['price_change_percent']
        
        print(f"✅ Data fetched successfully!")
        print(f"--------------------------------------------------")
        print(f"🪙 Asset        : {symbol_check}")
        print(f"💵 Live Price   : ${current_price:,.2f}")
        print(f"📊 24h Change   : {change_pct:+.2f}%")
        print(f"📈 24h High     : ${market_data['high']:,.2f}")
        print(f"📉 24h Low      : ${market_data['low']:,.2f}")
        print(f"--------------------------------------------------")

        # Trend analysis & dynamic TP/SL calculation logic
        print("🤖 AI Market Analysis:")
        if change_pct > 0:
            print("   Status : Bullish / Positive Momentum 🟢")
            tp1 = current_price * 1.015  # Target +1.5%
            tp2 = current_price * 1.030  # Target +3.0%
            sl = current_price * 0.990   # Risk limit -1.0%
        else:
            print("   Status : Bearish / Selling Pressure Watch 🔴")
            tp1 = current_price * 1.010  # Bounce target +1.0%
            tp2 = current_price * 1.020  # Bounce target +2.0%
            sl = current_price * 0.985   # Risk limit -1.5%

        print("\n🎯 Recommended Trading Zones & Risk Management:")
        print(f"   • Entry Area : ${current_price:,.2f} (Market Price)")
        print(f"   • Take Profit (TP 1) : ${tp1:,.2f} (+1.5%)")
        print(f"   • Take Profit (TP 2) : ${tp2:,.2f} (+3.0%)")
        print(f"   • Stop Loss (SL)     : ${sl:,.2f} (-1.0%)")
        print("==================================================")
        print("⚠️ Disclaimer: This analysis is automatically generated for simulation purposes.\n")

if __name__ == "__main__":
    main()
