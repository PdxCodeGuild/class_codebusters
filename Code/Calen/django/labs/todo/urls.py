from django.urls import path
from .views import delete, home, save, completed

app_name = 'todo'
urlpatterns = [
    path('', home, name='home'),
    path('save', save, name='save'),
    path('delete/<int:todo_id>', delete, name='delete'),
    path('completed/<int:todo_id>', completed, name='completed'),
]