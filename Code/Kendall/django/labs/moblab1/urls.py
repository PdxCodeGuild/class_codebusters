from django.urls import path
from . import views

app_name = 'moblab1'

urlpatterns = [
    path('', views.home, name='home'),
    path('save/', views.save, name='save'),
    path('<str:code>/', views.redirect, name='redirect')
]
