from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.home, name='home'),
    path('todos/', views.get_todos, name='get_todo'),
    path('create/', views.create_todo, name='create_todo'),
    path('update/', views.update_todo, name='update_todo'),
    path('delete/', views.delete_todo, name='delete_todo'),
]