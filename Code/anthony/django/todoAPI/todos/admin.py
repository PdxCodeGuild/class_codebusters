from todos.models import TodoItem, TodoPriority
from django.contrib import admin

from .models import TodoPriority, TodoItem

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(TodoPriority)
