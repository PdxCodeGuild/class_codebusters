from django.db import models
from django.db.models.fields import CharField, FloatField, IntegerField

# Create your models here.


class PokemonType(models.Model):

    name = CharField(max_length=15)



    def __str__(self):
        return self.name

class Pokemon(models.Model):

    number = CharField(max_length=5)
    name = CharField(max_length=25)
    height = FloatField()
    weight = FloatField()
    image_front = CharField(max_length=50)
    image_back = CharField(max_length=50)

    types = models.ManyToManyField(PokemonType, related_name='types')

    def __str__(self):
        return f'{self.number} | {self.name}'

