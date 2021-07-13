from django.urls import path
from .views import home


app_name = 'catbusters'
urlpatterns = [
    path('', home, name='home'),
]
