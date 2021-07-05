from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.home, name="home"),
    path('vote/<int:choice_id>/', views.vote, name="vote"),
    path('generate_choices/', views.generate_choices, name="generate_choices"),
    path('add_choices/', views.add_choices, name="add_choices")
]