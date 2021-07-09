from django.urls import path

from . import views

app_name = 'mob1'

urlpatterns = [
    path('', views.home, name="home"),
    path('save/', views.save, name="save"),
    path('<str:data>/', views.redir, name="redir")
]