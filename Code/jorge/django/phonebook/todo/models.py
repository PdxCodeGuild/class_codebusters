from django.db import models
from django.db.models.fields import CharField, DateTimeField

# Create your models here.


class Todoitem(models.Model):
    text = models.CharField(max_length=100)
    created_date = DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
