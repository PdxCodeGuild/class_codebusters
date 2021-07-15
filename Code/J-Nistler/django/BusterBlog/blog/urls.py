from django.urls import path
from .views import home, register, login_user, logout_user, profile, create

app_name='blog'
urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create/', create, name='create'),
    path('<str:username>/', profile, name="profile"),
]