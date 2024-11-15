import yfinance as yf

# Fetch stock data for a specific ticker (e.g., Apple: AAPL)
stock = yf.Ticker("AAPL")

# Get historical market data
historical_data = stock.history(period="1mo")  # Options: '1d', '5d', '1mo', '1y', etc.

print(historical_data)
