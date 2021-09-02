from django.db import models

# Create your models here.


class PokemonType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    image_front = models.CharField(max_length=150)
    image_back = models.CharField(max_length=150)
    types = models.ManyToManyField(PokemonType)

    def __str__(self):
        return self.name
