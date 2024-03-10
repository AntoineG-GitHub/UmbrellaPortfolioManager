from django.urls import include, re_path
from rest_framework import routers

from backend import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'holder', views.HolderViewSet)
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
    re_path('signup', views.signup),
    re_path('login',views.login),
    re_path('test_token',views.test_token)

    
    
]

urlpatterns += router.urls