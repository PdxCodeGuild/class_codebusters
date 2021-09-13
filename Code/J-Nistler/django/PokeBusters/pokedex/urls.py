from django.urls import path
from .views import home, all_pokemon

app_name = "pokedex"
urlpatterns = [
    path('', home, name="home"),
    path('all_pokemon/', all_pokemon, name="all_pokemon"),
]