from typing import Text
from django.db import models
from django.db.models import deletion

# Create your models here.


class TodoPriority(models.Model):
    text = models.CharField(max_length=20)
    rank = models.IntegerField(default=3)

    def __str__(self):
        return self.text


class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    created_Date = models.DateField(auto_now_add=True)
    completed_date = models.DateField(blank=True, null=True)
    priority = models.ForeignKey(TodoPriority, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.priority} - {self.text}'