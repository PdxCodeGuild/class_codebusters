from django.urls import path

from . import views

app_name = 'lab0'
urlpatterns = [
    path('', views.index, name='index')
]
