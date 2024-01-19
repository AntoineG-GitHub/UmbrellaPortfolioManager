import pandas as pd

class Holders: 

    def __init__(self, id) -> None:
        self.id = id
        self.holding_history = pd.DataFrame(columns=['date', 'amount'])
    
    def add_transaction(self):
        pass
