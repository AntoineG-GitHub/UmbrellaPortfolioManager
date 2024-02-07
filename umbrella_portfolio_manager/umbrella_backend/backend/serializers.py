from django.contrib.auth.models import Group, User
from rest_framework import serializers

from backend.models import Portfolio, Stock_Metadata, Stock_Portfolio


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = Portfolio
        fields = ['name',   'users']
class StockMetadataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock_Metadata
        fields = ['ticker', 'name', 'sector', 'currency', 'address']

class StockPortfolioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock_Portfolio
        fields = ['ticker', 'portfolio', 'name_stock', 'currency']