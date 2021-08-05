from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('', views.home, name='home'),
    path('all/', views.all_digimon, name='all_digimon' ),
    path('<str:mon>/', views.get_digimon, name='get_digimon')
]