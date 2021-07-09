from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
        path('', views.home, name='home'),
        path('register/', views.register, name='register'),
        path('login_user/', views.login_user, name='login_user'),
        path('profile/', views.profile, name='profile'),
        path('create/', views.create, name='create'),
]