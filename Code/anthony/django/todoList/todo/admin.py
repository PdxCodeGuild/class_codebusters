from django.contrib import admin

# Register your models here.
from .models import ItemPriority, TodoItem
admin.site.register(ItemPriority)
admin.site.register(TodoItem)