from django.urls import path
from .views import home_page, save


app_name = "todolistapp"
urlpatterns = [
    path("", home_page, name="home"),
    path("save/", save, name="save"),
]