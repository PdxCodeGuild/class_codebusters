from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ManyToManyField

# Create your models here.
class PokemonType (models.Model):
    name = models.CharField(max_length=25, unique=True)
    
    def __str__(self):
        return self.name

class Pokemon (models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=25)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = CharField(max_length=50)
    image_back = CharField(max_length=50)
    types = ManyToManyField(PokemonType, related_name="pokemontypes")
    
    def __str__(self):
        return self.name
