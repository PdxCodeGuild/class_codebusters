from django.urls import path
from .views import home, save

app_name = 'todo'

urlpatterns = [
    path('', home, name='home'),
    path('save/', save, name='save'),
]
