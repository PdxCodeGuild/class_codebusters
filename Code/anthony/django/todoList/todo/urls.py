from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('save/', views.save_todo, name="save_todo"),
    path('edit/', views.edit_todo, name="edit_todo")
]