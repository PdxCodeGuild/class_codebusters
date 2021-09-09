from django.contrib import admin
from .models import Question, Choice

# Register your models here.
# pretty please :) 

admin.site.register(Question)
admin.site.register(Choice)