from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Todo


def home_page(request):
    return render(request, 'todo/index.html')


def task_results(requests):
    tasks = Todo.objects.all()
    context = {
        'tasks': tasks
    }

    return render(requests, 'todo/tasks.html', context)


def save(request):
    task = Todo()
    form = request.POST

    task.task = form['task']

    task.save()
    return redirect('../')
