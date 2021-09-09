from django.urls import path
from .views import home_page, save_url, search_url

app_name = 'shortener'
urlpatterns = [
    path('', home_page, name='home'),
    path('save_url/', save_url, name='save_url'),
    path('<str:my_code>', search_url, name='search_url'),
]
