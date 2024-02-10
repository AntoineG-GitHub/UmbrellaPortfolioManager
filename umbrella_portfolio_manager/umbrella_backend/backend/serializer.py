from django.contrib.auth.models import Group
from rest_framework import serializers

from backend.models import User,Actors_transaction, Portfolio, Stock_Metadata, Stock_Portfolio, Stock_transactions, Stock_price, Actors_portfolio, Portfolio_Evolution, Actor_profit_Evolution, Actors_transaction


class UserSerializer(serializers.HyperlinkedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','url', 'username', 'email', 'groups','portfolio']
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
class UserSerializerforPortfolio(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    

    class Meta:
        model = Portfolio
        fields = ['id', 'name']
        
    
class StockMetadataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock_Metadata
        fields = ['ticker', 'name', 'sector', 'currency', 'address']

class StockPortfolioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock_Portfolio
        fields = ['ticker', 'portfolio', 'currency']
class Stock_transactionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock_transactions
        fields = ['id_transaction', 'ticker', 'quantity', 'transaction_date', 'portfolio_id', 'transaction_price', 'conversion_rate', 'transaction_price', 'charges']
class Stock_priceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock_price
        fields = ['ticker', 'date', 'price', 'currency']
class Actors_portfolioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actors_portfolio
        fields = ['actor', 'portfolio', 'total_amount']
class Portfolio_EvolutionSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Portfolio_Evolution
        fields = ['portfolio', 'date', 'total_value', 'total_profit']
class Actor_profit_EvolutionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor_profit_Evolution
        fields = ['actor', 'date', 'total_profit', 'holding_percentage']
class Actors_transactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actors_transaction
        fields = ['id_user', 'amount', 'transaction_date', 'portfolio_id']