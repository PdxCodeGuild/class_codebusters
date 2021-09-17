from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    is_cool = models.BooleanField()


def __str__(self):
    return f'{self.name} -- {self.age}'
