from django.urls import path
from . import views

app_name = 'pokedex'
urlpatterns = [
    path('', views.home, name='home'),
    path('details/<str:pokemon_name>', views.details, name='details'),
]