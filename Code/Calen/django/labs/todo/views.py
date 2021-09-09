from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import Todoitem

# Create your views here.

def home(request):

    context  = {
        'todoitems': Todoitem.objects.all()
    }

    return render(request, 'todo/index.html', context)


def save(request):
    # lets make a new instance
    new_item = Todoitem()
    #rename the post function because lazy
    form = request.POST

    # lets unpack this bad boi
    new_item.text = form['text'].title()

    new_item.save()

    return HttpResponseRedirect(reverse('todo:home'))


def completed(request, todo_id):
    # lets set completion
    item = Todoitem.objects.get(id=todo_id)
    item.completed = True
    item.save()
    print(item.completed)
    

    return HttpResponseRedirect(reverse('todo:home'))

def delete(request, todo_id):
    # deletion obvi
    item = Todoitem.objects.get(id=todo_id)
    item.delete()

    return HttpResponseRedirect(reverse('todo:home'))