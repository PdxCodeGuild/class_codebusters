from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import TodoItem, TodoPriority
import json

# Create your views here.
def home(request):
    return render(request, 'todos/index.html')

def get_todos(request):
    items = TodoItem.objects.all()

    json = {
        'todos': []
    }
    for item in items:
        json['todos'].append({
            'text': item.text,
            'completed_date': item.completed_date,
            'priority': item.priority.text
        })

    return JsonResponse(json)

def create_todo(request):
    data = request.body.decode("utf-8")
    print(json.load(data))

    return HttpResponse('Ok, received request')