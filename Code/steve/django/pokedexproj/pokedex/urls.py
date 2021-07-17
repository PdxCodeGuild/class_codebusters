from django.urls import path
from .views import all_pokes, home


app_name = 'pokedex'
urlpatterns = [
    path('', home, name='home'),
    path('all_pokes/<str:name>', all_pokes, name='all_pokes'),
]
