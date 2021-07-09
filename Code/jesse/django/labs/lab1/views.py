from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse

from .models import TodoItem

# Create your views here.
def home(request):
    items = TodoItem.objects.all()

    context = {
        'items': items
    }

    return render(request, 'lab1/index.html', context)

def save(request):
    name = request.POST['todo_text']
    todo = TodoItem(text=name)
    todo.save()
    print(request.POST)
    return HttpResponseRedirect(reverse('lab1:home'))