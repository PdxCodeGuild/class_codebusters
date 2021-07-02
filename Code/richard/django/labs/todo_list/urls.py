from django.urls import path
from . import views

app_name = 'todo_list'
urlpatterns = [
        path('', views.home, name='home'),
        path('add_form', views.add_form, name='add_form'),
        path('add', views.add_tasks, name='add'),
        path('<int:task_id>', views.complete_task, name='completed'),
        path('delete/<int:task_id>', views.delete_task, name='delete_task'),
]