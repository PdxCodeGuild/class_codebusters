from django.urls import path
from .views import home_page, all_contacts, save_contact

app_name = "contacts"
urlpatterns = [
    path("", home_page, name="home"),
    path("all/", all_contacts, name="all_contacts"),
    path("save_contact/", save_contact, name="save_contact")
]