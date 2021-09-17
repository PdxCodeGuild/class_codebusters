from .models import TodoItem
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def home(request):
    todos = TodoItem.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'todo/index.html', context)


def save(request):
    text = request.POST['text']
    todo = TodoItem(text=text)
    todo.save()
    return HttpResponseRedirect(reverse('todo:home'))
