import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf


# Get the apple stock
stock = yf.Ticker("AAPL")

# Fetch stock data
historical_data = stock.history(period="3mo")

# Calculate moving averages
historical_data["SMA_20"] = historical_data["Close"].rolling(window=20).mean()
historical_data["SMA_50"] = historical_data["Close"].rolling(window=50).mean()

# Plot stock prices with moving averages
historical_data[["Close", "SMA_20", "SMA_50"]].plot(figsize=(10, 6))
plt.title("Stock Price with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()
