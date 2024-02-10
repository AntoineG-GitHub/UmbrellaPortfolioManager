import pandas as pd

from portfolio.holders import Holders 
from portfolio.holders import Holders
from portfolio.stock import Stock 

class Portfolio:
    
    def __init__(self, id) -> None:
        self.id = id
        self.total_value = 0
        self.holders = {}
        self.portfolio = {}
        self.stocks = {}
        self.portfolio_transactions = pd.DataFrame(columns=['ticker', 'transactions_date', 'quantity', 
                                                        'transaction_price', 'conversation_rate', 
                                                        'transaction_price_euro', 'charge'])
        
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

    def update_holders_transactions(self, holder_id, date, amount: float):
        self.holders[holder_id].add_transaction(date, amount)

    def add_holder(self, holder_id):
        if holder_id not in self.holders.keys():
            self.holders[holder_id] = Holders(holder_id)
        else: 
            #update the current holder
            pass

    def add_stock_transactions(self, ticker: str, date, quantity: int, transaction_price: float,
                               conversation_rate: float, transaction_price_euro: float, charge: float):
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

    def update_all_history(self):
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
        pass

    