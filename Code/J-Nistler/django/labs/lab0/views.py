from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

# Create your views here.

def index (request):
    people = Person.objects.all()


    context = {
        "friends": people,
        "colors": ['green', 'blue', 'yellow', 'red']
    }

    return render(request, "lab0/index.html", context)