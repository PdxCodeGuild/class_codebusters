from django.urls import path
from . import views

app_name = 'list'
urlpatterns = [
    path('checklist/', views.checklist, name='checklist'),
    path('mycreate/', views.mycreate, name='mycreate')
]
