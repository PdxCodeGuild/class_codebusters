from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils import timezone
from .models import TodoItem, TodoPriority
import json

# Create your views here.
def home(request):
    return render(request, 'todos/index.html')


# CRUDL
# Create
def create_todo(request):
    body = request.body # byte string ->  b'101010101110'
    data = body.decode("utf-8") # json string -> '{"key": "value"}'
    todo_data = json.loads(data) # dictionary -> {"key": "value"}

    priority = TodoPriority.objects.get(value=int(todo_data['todoPriority']))

    todo = TodoItem()
    todo.text = todo_data['todoItem']
    todo.priority = priority
    todo.save()

    return HttpResponse('Ok, received request')
# Retrieve (single)
# No need to get single todo

# Update (single)
def update_todo(request):
    data = request.body.decode('utf-8')
    todo_id = json.loads(data)
    id = int(todo_id['todoId'])

    todo = TodoItem.objects.get(id=id)
    todo.completed_date = timezone.now()
    todo.save()

    return JsonResponse({'ok': True})


# Delete (single)
def delete_todo(request):
    data = request.body.decode('utf-8')
    todo_id = json.loads(data)
    id = int(todo_id['todoId'])

    todo = TodoItem.objects.get(id=id)
    todo.delete()

    return JsonResponse({'ok': True})



# List (all)
def get_todos(request):
    items = TodoItem.objects.all()

    json = {
        'todos': []
    }
    for item in items:
        json['todos'].append({
            'text': item.text,
            'completed_date': item.completed_date,
            'priority': item.priority.text,
            'id': item.id
        })

    return JsonResponse(json)
