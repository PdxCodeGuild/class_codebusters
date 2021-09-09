from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.home, name="home"),
    path('vote/<int:choice_id>/', views.vote, name="vote"),
    path('generate_choices/', views.generate_choices, name="generate_choices"),
    path('add_choices/', views.add_choices, name="add_choices"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('<str:username>/', views.user_polls, name="user_polls"),
]
