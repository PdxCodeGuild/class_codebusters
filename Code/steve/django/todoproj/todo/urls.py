from django.urls import path
from .views import home_page, save, task_results

app_name = 'todo'
urlpatterns = [
    path('', home_page, name='home'),
    path('task_results/', task_results, name='task_results'),
    path('save/', save, name='save'),
]
