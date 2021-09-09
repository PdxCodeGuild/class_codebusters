from django.contrib.auth import logout
from django.urls import path
from .views import home, details,type

app_name = 'pokedex'
urlpatterns = [
    path('', home, name='home'),
    path('<str:number>/', details, name='details'),
    path('types/<str:type>/', type, name='type'),

]