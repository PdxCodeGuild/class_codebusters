from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tasks

def home(request):
    NC_tasks = Tasks.objects.filter(completed = False)
    C_tasks = Tasks.objects.filter(completed = True)
    context = {
        'NC_tasks' : NC_tasks,
        'C_tasks' : C_tasks
    }
    return render(request, 'todo_list/index.html',context)

def add_form(request):
    return render(request, 'todo_list/form.html')

def add_tasks(request):
    tasks = Tasks()
    form = request.POST
    tasks.text = form['text']
    tasks.save()
    return redirect('../todo_list/')

def complete_task(request, task_id):
    completed_task = Tasks.objects.get(id=task_id)
    completed_task.completed = True
    completed_task.save()
    return redirect('../todo_list/')

def delete_task(request, task_id):
    deleted_task = Tasks.objects.get(id=task_id)
    deleted_task.delete()
    return redirect('../')