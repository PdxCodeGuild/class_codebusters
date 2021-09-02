from django.urls import path
# from .import views
# from .views import home, register, login_user, logout, profile, create 
from .import views 


app_name = 'blogpost'
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('create/', views.create, name='create'),
]


# path('create/', views.create, name='create'),