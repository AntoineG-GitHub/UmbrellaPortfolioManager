from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, default="default")
    users = models.ManyToManyField(User)

    def __str__(self):
        return f"Portfolio {self.pk}"

class Stock_Metadata(models.Model):
    ticker = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, null=False)
    sector = models.CharField(max_length=100, null=False)
    currency = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)

class Stock_Portfolio(models.Model):
    ticker = models.ForeignKey(Stock_Metadata, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    name_stock = models.CharField(max_length=100, null=False)
    currency = models.CharField(max_length=100, null=False)
