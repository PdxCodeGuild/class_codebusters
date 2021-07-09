from django.shortcuts import render
from django.http import HttpResponse
from .models import Todoitem

# Create your views here.


def home_page(request):
    myinstances = Todoitem.objects.all()
    context = {
        'message': 'Ok!'
    }
    return render(request, 'todo/index.html', context)
