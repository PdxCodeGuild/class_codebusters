from django.urls import path
from . import views

app_name = 'pokedex'
urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:poke_id>', views.details, name='details'),
]