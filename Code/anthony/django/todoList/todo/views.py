from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.utils import timezone

from .models import TodoItem, ItemPriority

# Create your views here.
def home_page(request):
    todos = TodoItem.objects.order_by('completed_date', '-priority__value')
    priorities = ItemPriority.objects.order_by('value')
    context = {
        'todos': todos,
        'priorities': priorities
    }
    return render(request, 'todo/index.html', context)

def save_todo(request):
    # Form data
    form = request.POST
    text = form['todo_text']
    priority_id = form['priority']
    print(form)
    priority = ItemPriority.objects.get(id=priority_id)

    # Assign values
    todo_item = TodoItem()
    todo_item.title = text
    todo_item.priority = priority
    # todo_item.save()

    return HttpResponseRedirect(reverse('todo:home_page'))

def edit_todo(request):
    form = request.POST
    text = form['todo_text']
    todo_id = form['todo_id']
    if 'completed' in form:
        completed = timezone.now()
    else:
        completed = None

    todo = TodoItem.objects.get(id=todo_id)
    todo.title = text
    todo.completed_date = completed
    todo.save()

    return HttpResponseRedirect(reverse('todo:home_page'))