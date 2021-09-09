from django.urls import path
from .views import contact_details, home_page, all_contacts, save_contact, search_contact

app_name = 'contacts'
urlpatterns = [
    path('', home_page, name='home'),
    path('all/', all_contacts, name='all_contacts'),
    path("save_contact/", save_contact, name="save_contact"),
    path("search/", search_contact, name="search_contact"),
    path("detail/<int:contact_id>/", contact_details, name="detail"),
]