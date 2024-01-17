from pydantic import AnyUrl, BaseModel, PrivateAttr
from datetime import date
import yfinance as yf
class Stock(BaseModel):
    """Class that gathers informatoin about the stock present in the portfolio; 
    Information is translated by the stock price history, the quantity, the buying dates, etc. 
    """
    ticker: str
    stock: yf.Ticker = PrivateAttr(default=None)
    hello: str
    class Config:
        # Ajoutez cette configuration pour autoriser les types arbitraires
        arbitrary_types_allowed = True
        extra = "allow"  # Permet d'ignorer les champs non déclarés dans le modèle

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_metadata()
        self.stock = yf.Ticker(self.ticker)
        # self.stock_history = self.load_price_history(self.ticker)

    def load_metadata(self):
        
        self.hello = "hello"

    def load_price_history(ticker, date_start, period):
        pass

    def add_transaction(buying_date, buying_price, quantity):
        pass

