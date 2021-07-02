from django.db import models

# Create your models here.


class MyModel(models.Model):
    myfield = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.myfield
