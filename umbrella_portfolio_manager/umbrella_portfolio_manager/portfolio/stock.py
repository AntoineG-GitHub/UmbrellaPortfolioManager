import yfinance as yf


class Stock:
    """Class that gathers information about the stock present in the portfolio; 
    Information is translated by the stock price history, the quantity, the buying dates, etc. 
    """

    def __init__(self, ticker):
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)
        self.load_metadata()

    def load_metadata(self):
        self.actions = self.stock.actions

    def load_price_history(ticker, date_start, period):
        pass

    def add_transaction(buying_date, buying_price, quantity):
        pass

