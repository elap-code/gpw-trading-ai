# stock_data.py – Datenanbindung an Yahoo Finance oder andere APIs
# stock_data.py – Holt Daten von Yahoo Finance
import yfinance as yf

class StockDataManager:
    def get_stock_data(self, symbol="KGH.WA", period="1mo", interval="1d"):
        stock = yf.Ticker(symbol)
        df = stock.history(period=period, interval=interval)
        return df
