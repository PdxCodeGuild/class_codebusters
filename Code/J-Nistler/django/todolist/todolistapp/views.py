from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import TodoItem

# Create your views here.
def home_page(request):

    ToDoItems = TodoItem.objects.all()

    context = {
        "todoitems": ToDoItems   
    }

    return render(request, 'todolistapp/index.html', context)

def save(request):

    listitem = TodoItem()

    form = request.POST

    listitem.item = form['item']

    listitem.save()

    return HttpResponseRedirect("../")