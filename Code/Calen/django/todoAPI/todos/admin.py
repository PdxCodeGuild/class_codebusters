
from django.contrib import admin
from .models import TodoItem, TodoPriority

# Register your models here.

admin.site.register(TodoItem)
admin.site.register(TodoPriority)