from django.db import models
from django.db.models.fields import BooleanField, CharField, DateTimeField

# Create your models here.


class Todoitem(models.Model):
    text = CharField(max_length=200)
    created_date = DateTimeField(auto_now_add=True)
    completed = BooleanField(null=True, default=False)

    def __str__(self):
        return self.text

