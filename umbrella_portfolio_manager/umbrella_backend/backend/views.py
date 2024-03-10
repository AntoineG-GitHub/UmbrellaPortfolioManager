from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group,User
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from backend.serializer import Actors_transactionSerializer, GroupSerializer, HolderSerializer, PortfolioSerializer, StockMetadataSerializer, StockPortfolioSerializer, Stock_transactionsSerializer, Stock_priceSerializer, Actors_portfolioSerializer, Portfolio_EvolutionSerializer, Actor_profit_EvolutionSerializer, Actors_transactionSerializer, UserSerializer
from backend.models import Holder,Actors_transaction, Portfolio, Stock_Metadata, Stock_Portfolio, Stock_transactions, Stock_price, Actors_portfolio, Portfolio_Evolution, Actor_profit_Evolution, Actors_transaction


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors,  status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
class HolderViewSet(viewsets.ModelViewSet):    
    queryset = Holder.objects.all()
    serializer_class = HolderSerializer
    permission_classes = [permissions.AllowAny]

class GroupViewSet(viewsets.ModelViewSet):    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]
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
    
    
