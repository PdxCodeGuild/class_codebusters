from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.http import HttpRequest
from .models import TodoItem, TodoPriority
import json
from django.utils import timezone
# Create your views here.


def home(request):
    return render(request, 'todos/index.html')

    # CRUDLE

# Create
def create_todo(request):
    
    body = request.body
    data = body.decode("utf-8")
    todo_data = json.loads(data)
    priority = TodoPriority.objects.get(rank=int(todo_data['todoPriority']))
    
    todo = TodoItem()
    todo.text = todo_data['todoItem']
    todo.priority = priority
    todo.save()

    return HttpResponse('got it')

# Retrieve

# Update

def update_todo(request):
    data = request.body.decode('utf-8')
    todo_id = json.loads(data)
    id = todo_id['todoID']

    todo = TodoItem.objects.get(id=int(id))
    todo.completed_date = timezone.now()
    todo.save()

    return JsonResponse({'ok':True})

# Delete

def delete_todo(request):
    data = request.body.decode('utf-8')
    todo_id = json.loads(data)
    id = int(todo_id['todoID'])

    todo = TodoItem.objects.get(id=id)
    todo.delete()
    return JsonResponse({'ok': True})


# List
def get_todos(request):
    items = TodoItem.objects.all()

    output = {
        'todos': [],
    }
    for item in items:
        output['todos'].append({
            'text': item.text,
            'completed_date': item.completed_date,
            'priority': item.priority.text,
            'id': item.id,
        })
    return JsonResponse(output)
