from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {
        'name': 'Joe',
        'is_cool': True,
        'colors': ['red', 'blue', 'green']
    }
    return render(request, 'firstApp/index.html', context)