from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from backend.serializer import Actors_transactionSerializer, GroupSerializer, PortfolioSerializer, StockMetadataSerializer, StockPortfolioSerializer, UserSerializer, Stock_transactionsSerializer, Stock_priceSerializer, Actors_portfolioSerializer, Portfolio_EvolutionSerializer, Actor_profit_EvolutionSerializer, Actors_transactionSerializer
from backend.models import Actors_transaction, Portfolio, Stock_Metadata, Stock_Portfolio, Stock_transactions, Stock_price, Actors_portfolio, Portfolio_Evolution, Actor_profit_Evolution, Actors_transaction


class UserViewSet(viewsets.ModelViewSet):    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class= PortfolioSerializer
    permission_classes = [permissions.AllowAny]
class StockMetadataViewSet(viewsets.ModelViewSet):
    queryset = Stock_Metadata.objects.all()
    serializer_class = StockMetadataSerializer
    permission_classes = [permissions.AllowAny]

class StockPortfolioViewSet(viewsets.ModelViewSet):
    queryset = Stock_Portfolio.objects.all()
    serializer_class = StockPortfolioSerializer
    permission_classes = [permissions.AllowAny]
class Stock_transactionsViewSet(viewsets.ModelViewSet):
    queryset = Stock_transactions.objects.all()
    serializer_class = Stock_transactionsSerializer
    permission_classes = [permissions.AllowAny]
class Stock_priceViewSet(viewsets.ModelViewSet):
    queryset = Stock_price.objects.all()
    serializer_class = Stock_priceSerializer
    permission_classes = [permissions.AllowAny]
class Actors_portfolioViewSet(viewsets.ModelViewSet):
    queryset = Actors_portfolio.objects.all()
    serializer_class = Actors_portfolioSerializer
    permission_classes = [permissions.AllowAny]
class Portfolio_EvolutionViewSet(viewsets.ModelViewSet):
    queryset = Portfolio_Evolution.objects.all()
    serializer_class = Portfolio_EvolutionSerializer
    permission_classes = [permissions.AllowAny]
class Actor_profit_EvolutionViewSet(viewsets.ModelViewSet):
    queryset = Actor_profit_Evolution.objects.all()
    serializer_class = Actor_profit_EvolutionSerializer
    permission_classes = [permissions.AllowAny]
class Actors_transactionViewSet(viewsets.ModelViewSet):
    queryset = Actors_transaction.objects.all()
    serializer_class = Actors_transactionSerializer
    permission_classes = [permissions.AllowAny]
    
    
