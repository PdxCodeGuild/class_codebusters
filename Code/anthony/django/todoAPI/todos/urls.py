from django.urls import path

from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.home, name="home"),
    # Create
    path('create/', views.create_todo, name="create_todo"),
    # Update
    path('update/', views.update_todo, name="update_todo"),
    # Delete
    path('delete/', views.delete_todo, name="delete_todo"),
    # List
    path('todos/', views.get_todos, name="get_todos"),
]