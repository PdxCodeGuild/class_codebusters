from django.db import models

# Create your models here.
class TodoItem(models.Model):
    item = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.item}"