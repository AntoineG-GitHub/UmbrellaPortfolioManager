from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from backend.serializers import GroupSerializer, PortfolioSerializer, StockMetadataSerializer, StockPortfolioSerializer, UserSerializer
from backend.models import Portfolio, Stock_Metadata, Stock_Portfolio


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
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
