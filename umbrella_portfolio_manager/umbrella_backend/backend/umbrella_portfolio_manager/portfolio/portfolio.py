import pandas as pd

from portfolio.holders import Holders 
from portfolio.holders import Holders
from portfolio.stock import Stock 

class Portfolio:
    
    def __init__(self, id) -> None:
        self.id = id
        self.total_value = 0
        self.holders = {}
        self.holders_percenatge = {}
        self.portfolio = {}
        self.stocks = {}
        self.dict_evolution = {}
        self.periods = []
        self.portfolio_transactions = pd.DataFrame(columns=['ticker', 'transactions_date', 'quantity', 
                                                        'transaction_price', 'conversation_rate', 
                                                        'transaction_price_euro', 'charge'])
        self.total_inputs = 0

    def update_total_value(self):
        for value in self.stocks.values() :
            self.total_value =+ value.quantity*value.minute_price        

    def update_portfolio(self, ticker: str, quantity: int): 
        if ticker in self.portfolio.keys():
           self.portfolio[ticker] += quantity
        else :
            self.portfolio[ticker]= quantity

    def update_holders_benefits(self):
        pass

    def add_holders_transactions(self, holder_id, date, amount: float):
        
        if holder_id in self.holders.keys():
            self.holders[holder_id].add_transaction(date, amount)
            # self.holders[holder_id].update_holder_amount(amount) # pas besoin car déjà fait coté class de holder! 
        else: 
            self.holders[holder_id] = Holders(id = holder_id)
            self.holders[holder_id].add_transaction(date, amount)


    def compute_holders_percentage(self):
        pass

    def compute_holders_percentage_historic(self):
        self.holders_percentage_historic = pd.DataFrame()

        for id, holder in self.holders.items():
            # Copy the DataFrame to avoid modifying the original DataFrame in holder.evolution
            temp_df = holder.evolution.copy()

            # Ensure the 'date' column is set for alignment. This might not be necessary if it's already the index
            # If 'date' is not the index, consider setting it as the index or ensuring it's consistent across all DataFrames
            # temp_df.set_index('date', inplace=True)
            
            # Rename the 'amount' column to 'amount_{id}'
            temp_df.rename(columns={'amount': f'amount_{id}'}, inplace=True)
            
            # If using 'date' as an index, you might not need this step
            # If 'date' is a column and you want it in every chunk of the DataFrame, ensure it's included or managed as an index
            
            # Concatenate with the total_table
            if self.holders_percentage_historic.empty:
                self.holders_percentage_historic = temp_df
            else:
                # Use axis=1 to concatenate column-wise
                self.holders_percentage_historic = pd.concat([self.holders_percentage_historic, temp_df], axis=1)
        
        # Calculate the total amount across all 'amount_{id}' columns
        self.holders_percentage_historic['total_amount'] = self.holders_percentage_historic.filter(like='amount').sum(axis=1)

        # Calculate the percentage that each 'amount_{id}' represents in its own column
        for id in self.holders.keys():
            self.holders_percentage_historic[f'percentage_{id}'] = (self.holders_percentage_historic[f'amount_{id}'] / self.holders_percentage_historic['total_amount']) * 100

            
    def add_stock_transactions(self, ticker: str, date, quantity: int, transaction_price: float,
                               conversation_rate: float, transaction_price_euro: float, charge: float):
        if date not in self.periods:
            self.periods.append(date)
        if ticker in self.stocks.keys():
            self.stocks[ticker].update_quantity(quantity)
        else: 
            self.stocks[ticker] = Stock(ticker = ticker, quantity = quantity)
        
        new_stocks = pd.DataFrame([{'ticker': ticker, 'transactions_date': date, 'quantity': quantity, 
                                                        'transaction_price': transaction_price, 'conversation_rate': conversation_rate, 
                                                        'transaction_price_euro': transaction_price_euro, 'charge':charge}])
        self.portfolio_transactions = pd.concat([self.portfolio_transactions, new_stocks])
        
        self.stocks[ticker].add_transaction(date, quantity, transaction_price,
                               conversation_rate, transaction_price_euro, charge)
       
        self.update_portfolio(ticker, quantity)

    def update_all_history(self, date_end):
        history_stocks = {}
        periods = self.portfolio_transactions['transactions_date'].unique()
        print(periods)
        for index, row in self.portfolio_transactions.iterrows():
            if row['ticker'] in history_stocks.keys():
                history_stocks[row['ticker']].update_quantity(row['quantity'])
            else: 
                history_stocks[row['ticker']] = Stock(ticker = row['ticker'], quantity = row['quantity'])
            history_stocks[row['ticker']].update_dict_evolution_historic(date_start = row['transactions_date'], date_end = '2024-01-01')
        print(index, row)

        for date in periods: 
            pass
        # pour chaque date dans les periodes, on recrée une table 
        # d'historique pour chaque stock de la transaction 

    def update_portfolio_evolution(self):
        
        for period in self.periods:
            total_stocks = pd.DataFrame()
            for key, value in self.stocks.items():
                total_stocks =pd.concat([total_stocks, value.dict_evolution[str(period)]['transaction_price_euro']*value.dict_evolution[str(period)]['quantity']], axis=1)
                total_stocks['total_value'] = total_stocks.sum(axis=1)
                self.dict_evolution[period] = pd.DataFrame(total_stocks['total_value'], columns = ['total_value'])
