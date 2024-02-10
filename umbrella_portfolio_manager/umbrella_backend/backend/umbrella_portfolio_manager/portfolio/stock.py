import yfinance as yf
import pandas as pd
import datetime

class Stock:
    """Class that gathers information about the stock present in the portfolio; 
    Information is translated by the stock price history, the quantity, the buying dates, the profit, etc. 
    """

    def __init__(self, ticker, quantity) -> None:
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)
        self.minute_price = 0
        self.quantity = quantity
        self.profit = 0
        self.stock_transactions = pd.DataFrame(columns=['transactions_date', 'quantity', 
                                                        'transaction_price', 'conversation_rate', 
                                                        'transaction_price_euro', 'charge'])
        self.dict_evolution = {}


        self._load_metadata()
        self.exchange_ticker = yf.Ticker(self._find_exchange_ticker())
        # self.transactions = pd.DataFrame(columns=['ticker', 'buying_date', 'buying_price', 'quantity'])
        self._load_ohlcv_history()
        self.update_minute_price()
        

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
        self.forex = self.stock.info.get('financialCurrency', '')
        self.info = self.stock.info  # all info possible from yfinance

    def _find_exchange_ticker(self):
        """Finds the appropriate ticker for currency exchange with Euro"""
        if self.forex == 'USD':
            return 'EURUSD=X'  # Example ticker for USD to EUR exchange rate
        elif self.forex == 'GBP':
            return 'EURGBP=X'  # Example ticker for GBP to EUR exchange rate
        # Add more currencies as needed

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
         
         self.minute_price = self.stock.history(period='1d')['Close'].iloc[-1]

    def add_transaction(self, date, quantity: int, transaction_price: float,
                               conversation_rate: float, transaction_price_euro: float, charge: float):
        new_stock = pd.DataFrame([{ 'transactions_date': date, 'quantity': quantity, 
                                                        'transaction_price': transaction_price, 'conversation_rate': conversation_rate, 
                                                        'transaction_price_euro': transaction_price_euro, 'charge':charge}])
        self.stock_transactions = pd.concat([self.stock_transactions, new_stock])

        self.dict_evolution[date] = pd.DataFrame([{"date": date, "quantity": self.quantity, "price" : transaction_price, 
                                                   'transaction_price_euro' : transaction_price_euro, 'conversion_rate': conversation_rate}])
        self.dict_evolution[date].index = self.dict_evolution[date]["date"]
        self.dict_evolution[date] = self.dict_evolution[date].drop('date', axis=1)
        
    def update_dict_evolution() :
        pass

    def update_dict_evolution_historic(self, date_start, date_end) :
        """
        Update the historical evolution of a stock in the dictionary `dict_evolution`.

        This function retrieves historical data for both the stock price and the currency conversion rate
        for a specified date range. It then calculates the transaction price in euros and updates the 
        `dict_evolution` attribute with this information.

        Args:
            date_start (str or datetime): The start date for fetching historical data.
            date_end (str or datetime): The end date for fetching historical data.

        Returns:
            None: This function updates the `dict_evolution` attribute in-place.
        """
        closing_price = self.stock.history(start= date_start , end=date_end)["Close"]
        closing_price = closing_price.to_frame(name='price')
        closing_price.index = closing_price.index.date

        closing_conversion_rate = self.exchange_ticker.history(start=date_start, end=date_end)["Close"]
        closing_conversion_rate = closing_conversion_rate.to_frame(name='conversion_rate')
        closing_conversion_rate.index = closing_conversion_rate.index.date

        merged_data = pd.merge(closing_price, closing_conversion_rate, left_index=True, right_index=True) 
        merged_data['transaction_price_euro'] = merged_data['price'] / merged_data['conversion_rate']
        merged_data['quantity'] = self.quantity      
        if date_start in self.dict_evolution.keys() : 
            self.dict_evolution[date_start] = pd.concat([self.dict_evolution[date_start], merged_data])
        else :
            self.dict_evolution[date_start] =  merged_data


    def update_quantity(self, quantity):
        self.quantity += quantity
