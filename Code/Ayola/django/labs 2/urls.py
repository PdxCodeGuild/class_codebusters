"""labs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lab1 import views as views1
from lab2 import views as views2
from lab3 import views as views3


urlpatterns = [

    path('admin/', admin.site.urls),
    path('index',views1.index,name='index'),
    path('add',views1.add_item,name='add_item'),
    path('profile', views2.profile, name = 'profile'),
    path('login', views2.login, name = 'login'),
    path('sign_up',views2.sign_up,name='sign_up'),
    path('add_user',views2.add_user,name='add_user'),
    path('add_post',views2.add_post,name='add_post'),
    path('pokelist',views3.pokelist,name='pokelist'),
    path('details',views3.details,name='details')



]
