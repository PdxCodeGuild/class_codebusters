from django.urls import path

from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.home, name="home"),
    path('todos/', views.get_todos, name="get_todos"),
    path('create/', views.create_todo, name="create_todo")
]