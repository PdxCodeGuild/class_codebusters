from django.db import models
from django.db.models.fields import DateTimeField


class Todo(models.Model):
    task = models.CharField(max_length=50)
    created_date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task
