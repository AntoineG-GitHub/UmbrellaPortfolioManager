import pandas as pd

class Holders: 

    def __init__(self, id, amount) -> None:
        self.id = id
        self.amount = amount
        self.holding_history = {}
        self.transactions = pd.DataFrame(columns=['date', 'amount'])
        self.dict_evolution = {}
    
    def add_transaction(self, date, amount: float):
        new_transaction = pd.DataFrame([{'date': date, 'amount': amount}])
        self.transactions = pd.concat([self.transactions, new_transaction])
        
        self.holding_history[date] = pd.DataFrame([{'date': date, 'amount': amount}])
        self.holding_history[date].index = self.holding_history[date]["date"]
        self.holding_history[date] = self.holding_history[date].drop('date', axis=1)

    def update_holder_amount(self, amount):
        self.amount += amount

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
        # Create a DataFrame with a date range
        dates = pd.date_range(start=date_start, end=date_end, freq='D')
        # Create a DataFrame with dates and repeated amount
        data = {'date': dates, 'amount': self.amount}
        df = pd.DataFrame(data)
   
        if date_start in self.dict_evolution.keys() : 
            self.dict_evolution[date_start] = pd.concat([self.dict_evolution[date_start], df])
        else :
            self.dict_evolution[date_start] =  df
