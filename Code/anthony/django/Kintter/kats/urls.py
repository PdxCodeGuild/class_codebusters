from django.urls import path
from .views import home, get_cat, all_cats, vote_down, vote_up

app_name = "kats"
urlpatterns = [
    path('', home, name="home"),
    path('get_cats/', get_cat, name="get_cat"),
    path('view_all/', all_cats, name="view_all"),
    path('updoot/<int:cat_id>/', vote_up, name="updoot"),
    path('downdoot/<int:cat_id>/', vote_down, name="downdoot"),
]