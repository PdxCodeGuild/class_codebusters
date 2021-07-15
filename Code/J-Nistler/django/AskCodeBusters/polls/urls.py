from django.urls import path
from .views import home, vote, generate_choices, add_choices, signup, login_user, logout_user, user_polls


app_name = "polls"
urlpatterns = [
    path('', home, name="home"),
    path('vote/<int:choice_id>/', vote, name="vote"),
    path('generate_choices/', generate_choices, name="generate_choices"),
    path('add_choices/', add_choices, name="add_choices"),
    path('signup/', signup, name="signup"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('<str:username>/', user_polls, name="user_polls"),
]