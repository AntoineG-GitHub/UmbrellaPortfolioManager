from django.contrib.auth.models import User
from django.db import models
    
class Portfolio(models.Model):
    name = models.CharField(max_length=100, null=False, default="default")     
class User(User):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
class Stock_Metadata(models.Model):
    ticker = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, null=False)
    sector = models.CharField(max_length=100, null=False)
    currency = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)

class Stock_Portfolio(models.Model):
    ticker = models.ForeignKey(Stock_Metadata, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    currency = models.CharField(max_length=100, null=False)
    quantity = models.FloatField(null=False,default=0)
class Stock_price(models.Model):
    ticker = models.ForeignKey(Stock_Metadata, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.FloatField(null=False)
    currency = models.CharField(max_length=100, null=False)
class Actors_portfolio(models.Model):
    actor = models.ForeignKey(User, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    total_amount = models.FloatField(null=False)
class Portfolio_Evolution(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    date = models.DateField()
    total_value = models.FloatField(null=False)
    total_profit = models.FloatField(null=False)
class Actor_profit_Evolution(models.Model):
    actor = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    total_profit = models.FloatField(null=False)
    holding_percentage = models.FloatField(null=False)
class Actors_transaction(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(null=False)
    transaction_date = models.DateField()
    portfolio_id = models.ForeignKey(Actors_portfolio, on_delete=models.CASCADE)
class Stock_transactions(models.Model):
    id_transaction = models.BigAutoField(primary_key=True)
    ticker = models.ForeignKey(Stock_Metadata, on_delete=models.CASCADE)
    quantity = models.FloatField(null=False)
    transaction_date = models.DateField()
    portfolio_id = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    transaction_price = models.FloatField(null=False)
    conversion_rate = models.FloatField(null=False)
    transaction_price = models.CharField(max_length=100, null=False)
    charges = models.FloatField(null=False)
    