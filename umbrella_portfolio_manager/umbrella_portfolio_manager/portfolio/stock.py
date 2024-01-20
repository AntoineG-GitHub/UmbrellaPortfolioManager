import yfinance as yf
import pandas as pd
import datetime

class Stock:
    """Class that gathers information about the stock present in the portfolio; 
    Information is translated by the stock price history, the quantity, the buying dates, etc. 
    """

    def __init__(self, ticker) -> None:
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)
        self._load_metadata()
        self.transactions = pd.DataFrame(columns=['ticker', 'buying_date', 'buying_price', 'quantity'])
        self._load_ohlcv_history()
        self.quantity = 0

    def _load_metadata(self) -> None:
        """
        Load metadata for the stock.
        Populates mutiples attributes based on the stock using yahoo finance package. 
        
        Returns:
            None
        """
        self.name = self.stock.info.get('longName', '')
        self.sector = self.stock.info.get('sector', '')
        self.dividens = self.stock.actions[['Dividends']]
        self.info = self.stock.info  # all info possible from yfinance

    def _load_ohlcv_history(self) -> None:
        """
        Load historical Open, High, Low, Close, and Volume (OHLCV) data for the stock.

        Fetches the OHLCV data for the stock within the last year (365 days) from the current date.

        Populates the following attribute:
        - `self.ohlcv_history`: DataFrame containing OHLCV data with columns 'Open', 'High', 'Low', 'Close', and 'Volume'.

        Returns:
            None
        """
        start_date = datetime.datetime.now() - datetime.timedelta(days=365)
        end_date = datetime.datetime.now()
        self.ohlcv_history = self.stock.history(start=start_date, end=end_date)[['Open', 'High', 'Low', 'Close', 'Volume']]
    
    def update_ohlcv_history(self):
        pass

    def update_metadata(self):
        pass

    def update_minute_price(self):
        pass

    def add_transaction(buying_date, buying_price, quantity):
        pass
