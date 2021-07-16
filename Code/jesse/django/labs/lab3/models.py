from django.db import models

# Create your models here.
class PokemonType(models.Model):
    name =  models.CharField(max_length=20)

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=20)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.CharField(max_length=50)
    image_back = models.CharField(max_length=50)
    types = models.ManyToManyField(PokemonType)