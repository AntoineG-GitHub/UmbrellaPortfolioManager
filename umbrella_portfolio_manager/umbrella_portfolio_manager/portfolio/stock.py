from pydantic import BaseModel
from datetime import date

class Stock(BaseModel):
    """Class that gathers informatoin about the stock present in the portfolio; 
    Information is translated by the stock price history, the quantity, the buying dates, etc. 
    """
    ticker: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.stock_history = self.load_price_history(self.ticker)

    def load_metadata(ticker):
        pass

    def load_price_history(ticker, date_start, period):
        pass

    def add_transaction(buying_date, buying_price, quantity):
        pass

