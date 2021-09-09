from django.urls import path
from . import views

app_name = 'cat_api'
urlpatterns = [
    path('', views.home, name='home'),
    path('random/', views.random, name='random'),
    path('category/', views.category, name='category')
]
