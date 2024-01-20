import pandas as pd 

class Portfolio:
    
    def __init__(self, id) -> None:
        self.id = id
        self.total_value = 0
        self.holders = []
        self.portfolio = []
        self.stock_transactions = pd.DataFrame(columns=['date', 'ticker', 'transactions_date', 'quantity', 
                                                        'transaction_price', 'conversation_rate', 
                                                        'transaction_price_euro', 'charge'])
        
    def load_total_value(self):
        pass

    def update_total_value(self):
        pass

    def load_holders_benefits(self):
        pass

    def update_holders_benefits(self):
        pass

    def update_holders_transactions(self):
        pass

    def add_holder(self):
        pass

    def add_stock_transactions(self, ticker: str, date, quantity: int, transaction_price: float,
                               conversation_rate: float, transaction_price_euro: float, charge: float):
        pass