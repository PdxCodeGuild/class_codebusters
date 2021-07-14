from django.urls import path
from .views import home_page, redir, save

app_name = "shortener"
urlpatterns = [
    path('', home_page, name='home'),
    path('save/', save, name="save"),
    path('<str:data>/', redir, name="redir")
]
