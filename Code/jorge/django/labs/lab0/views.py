from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {
        'name': 'Joe'
    }
    return render(request, 'lab0/index.html', context)
