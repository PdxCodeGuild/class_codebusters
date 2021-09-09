from django.urls import path
from . import views

app_name = 'lab1'

urlpatterns = [
    path('', views.home, name='home'),
    path('save/', views.save, name='save')
]