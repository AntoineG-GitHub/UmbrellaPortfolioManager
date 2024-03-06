from django.test import TestCase
from django.contrib.auth.models import User
from .models import Portfolio, Holder

class PortfolioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crée un utilisateur pour les tests
        cls.test_user = User.objects.create_user(username='testuser', password='12345')
        cls.test_portfolio = Portfolio.objects.create(name='Test Portfolio')
        
        cls.test_user.save()
        cls.test_portfolio.save()
    def test_portfolio_holder_relationship(self):   

        # Créer un holder associé à l'utilisateur de test
        holder = Holder.objects.create(user=self.test_user, portfolio=self.test_portfolio)

        # Récupérer le portefeuille associé au holder
        holder_portfolio = holder.portfolio

        # Vérifier que le portefeuille associé est bien celui que nous avons créé
        self.assertEqual(self.test_portfolio, holder_portfolio)
    def test_portfolio_wrong_relationship(self):
        wrong_user =  User.objects.create_user(username='Thomas', password='12345')
        other_test_portfolio = Portfolio.objects.create(name='Otherportfolio')
        holder = Holder.objects.create(user=wrong_user, portfolio=other_test_portfolio)
        holder_portfolio = holder.portfolio
        # Vérifie que les 2 holder(celui crée mtn et celui de l'instance ne sont pas les même 
        self.assertNotEqual(self.test_portfolio, holder_portfolio)
   
    
    

