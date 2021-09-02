from django.urls import path
from . import views

app_name = 'pokedex'
urlpatterns = [
    path('', views.home, name='home'),
    path('info/<int:poke_id>/', views.info, name='info'),
]
