from django.shortcuts import render, redirect
from . import models

# Create your views here.


def index(request):
    
    items = models.TodoItem.objects.all()
    context = dict()
    context['items'] = items
    return render(request, "display.html", context = context)



def add_item(request):
    text = request.POST.get('text')
    item = models.TodoItem.objects.create(text=text)
    item.save()


    return redirect('index')
