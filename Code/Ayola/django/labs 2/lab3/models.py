from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class PokemonType(models.Model):

    name = models.CharField(max_length=500, primary_key=True)


class Pokemon(models.Model):
    
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.CharField(max_length=1000,null=True)
    image_back = models.CharField(max_length=1000,null=True)
    types = models.ManyToManyField(PokemonType)
