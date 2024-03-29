from django.urls import include, path
from rest_framework import routers

from backend import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'portfolio', views.PortfolioViewSet)
router.register(r'stock-metadata', views.StockMetadataViewSet)
router.register(r'stock-portfolio', views.StockPortfolioViewSet)
router.register(r'stock-transactions', views.Stock_transactionsViewSet)
router.register(r'stock-price', views.Stock_priceViewSet)
router.register(r'actors-portfolio', views.Actors_portfolioViewSet)
router.register(r'portfolio-evolution', views.Portfolio_EvolutionViewSet)
router.register(r'actor-profit-evolution', views.Actor_profit_EvolutionViewSet)
router.register(r'actors-transaction', views.Actors_transactionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls