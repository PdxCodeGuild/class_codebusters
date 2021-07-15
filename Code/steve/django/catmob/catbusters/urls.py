from django.urls import path
from .views import home, all, up_vote, down_vote


app_name = 'catbusters'
urlpatterns = [
    path('', home, name='home'),
    path('all/', all, name="all"),
    path('up_vote/<int:cat_id>/', up_vote, name="up_vote"),
    path('down_vote/<int:cat_id>/', down_vote, name="down_vote"),
]
