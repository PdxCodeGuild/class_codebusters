from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('create_blog/', views.create_blog, name='create_blog'),
]
