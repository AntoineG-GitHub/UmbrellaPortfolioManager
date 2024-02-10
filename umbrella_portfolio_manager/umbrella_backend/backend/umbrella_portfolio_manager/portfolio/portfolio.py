import pandas as pd

from portfolio.holders import Holders 

class Portfolio:
    
    def __init__(self, id) -> None:
        self.id = id
        self.total_value = 0
        self.holders = {}
        self.portfolio = {}
        self.stock_transactions = pd.DataFrame(columns=['ticker', 'transactions_date', 'quantity', 
                                                        'transaction_price', 'conversation_rate', 
                                                        'transaction_price_euro', 'charge'])
        
    def load_total_value(self):
        pass

    def update_portfolio(self, ticker: str, quantity: int): 
        if ticker in self.portfolio.keys():
           self.portfolio[ticker] += quantity
        else :
            self.portfolio[ticker]= quantity

    def update_total_value(self):
        pass

    def load_holders_benefits(self):
        pass

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
        
        # Call Stock function to update the whole object
        new_stocks = pd.DataFrame([{'ticker': ticker, 'transactions_date': date, 'quantity': quantity, 
                                                        'transaction_price': transaction_price, 'conversation_rate': conversation_rate, 
                                                        'transaction_price_euro': transaction_price_euro, 'charge':charge}])
        self.stock_transactions = pd.concat([self.stock_transactions, new_stocks])
 
        self.update_portfolio(ticker, quantity)