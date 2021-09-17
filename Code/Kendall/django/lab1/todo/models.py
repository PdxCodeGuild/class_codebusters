from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class TodoItem(models.Model):
    text = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
