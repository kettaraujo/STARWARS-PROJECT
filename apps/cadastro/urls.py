from django.urls import path
from .views import lista_jedi, criar_jedi

urlpatterns = [
    path('jedi/', lista_jedi, name='lista_jedi'),
    path('jedi/novo/', criar_jedi, name='criar_jedi'),
]