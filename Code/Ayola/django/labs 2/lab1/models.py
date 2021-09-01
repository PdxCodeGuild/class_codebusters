from django.db import models

# Create your models here.

class TodoItem(models.Model):

    text = models.CharField(max_length= 1000)
    date = models.DateTimeField(auto_now_add=True)