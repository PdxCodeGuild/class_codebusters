from django.urls import path
from . import views

app_name = 'firstApp'

urlpatterns = [
    path('', views.index, name='index'),
]
