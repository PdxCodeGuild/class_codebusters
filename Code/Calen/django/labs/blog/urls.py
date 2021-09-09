from django.contrib.auth import logout
from django.urls import path
from .views import create, home, login_page, profile_page, register, profile_page, logout_user

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile_page, name='profile'),
    path('register/', register, name='register'),
    path('login/', login_page, name='login'),
    path('create/', create, name='create'),
    path('logout/', logout_user, name='logout'),

]