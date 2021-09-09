from django.urls import path
from .views import home

app_name = 'showcase'
urlpatterns = [
    path('', home, name='home'),
]