from django.urls import path
from .views import lista_treinamentos, lista_missoes

urlpatterns = [
    path('treinamentos/', lista_treinamentos, name='lista_treinamentos'),
    path('missoes/', lista_missoes, name='lista_missoes'),
]