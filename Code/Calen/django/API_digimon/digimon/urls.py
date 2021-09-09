from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.home, name='home'),
    path('digimon/all/', views.all_digimon, name='all'),
    path('digimon/<str:mon>/', views.get_digimon, name='get_digimon'),

]