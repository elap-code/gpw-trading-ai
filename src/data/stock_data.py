# stock_data.py – Datenanbindung an Yahoo Finance oder andere APIs
# stock_data.py – Holt Daten von Yahoo Finance
import yfinance as yf

class StockDataManager:
    def get_current_price(self, symbol):
        ticker = yf.Ticker(symbol)
        todays_data = ticker.history(period="1d")
        return todays_data["Close"].iloc[-1]

    def get_history(self, symbol, period="1mo"):
        ticker = yf.Ticker(symbol)
        return ticker.history(period=period)
