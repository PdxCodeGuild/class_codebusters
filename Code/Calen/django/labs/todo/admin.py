from django.contrib import admin

# Register your models here.


from .models import Todoitem

admin.site.register(Todoitem)