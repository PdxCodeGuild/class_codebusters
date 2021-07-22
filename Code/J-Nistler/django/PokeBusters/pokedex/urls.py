from django.urls import path
from .views import home

app_name = "pokedex"
urlpatterns = [
    path('', home, name="home"),
]