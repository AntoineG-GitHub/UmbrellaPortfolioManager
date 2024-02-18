import pandas as pd

class Holders: 
    """
    Represents holders in portfolios.
    """

    def __init__(self, id) -> None:
        """
        Initializes a Holders instance based on the id.

        Args:
        - id: Identifier for the holders.
        """
        self.id = id
        self.amount = 0
        self.transactions = pd.DataFrame(columns=['date', 'amount'])
        self.evolution = pd.DataFrame(columns=['amount']).rename_axis('date')
    
    def add_transaction(self, date, amount: float):
        """
        Adds a transaction to the holder's record.
        This will update the transactions table and the evolution table as well as the amount parameter.

        Args:
        - date: Date of the transaction.
        - amount: Amount of the transaction.
        """
        new_transaction = pd.DataFrame([{'date': date, 'amount': amount}])
        new_holdings = pd.DataFrame({'amount': self.amount+amount}, index=[pd.to_datetime(date)])
        self.transactions = pd.concat([self.transactions, new_transaction])
        self.evolution = pd.concat([self.evolution, new_holdings])
        self.update_holder_amount(amount)

    def update_holder_amount(self, amount): 
        """
        Updates the current total amount held by the holder.

        Args:
        - amount: Amount to be added or subtracted.
        """
        self.amount += amount

    def update_dict_evolution_historic(self, date_start, date_end) :
        """
        Updates the historic evolution of the holder's holdings.

        Args:
        - date_start: Start date for the historic evolution.
        - date_end: End date for the historic evolution.
        """
        dates = pd.date_range(start=date_start, end=date_end, freq='D')
        df = pd.DataFrame({'amount': self.amount}, index=dates)
        self.evolution = pd.concat([self.evolution, df])
