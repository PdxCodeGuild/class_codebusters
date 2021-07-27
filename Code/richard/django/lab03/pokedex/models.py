from django.db import models

class PokemonType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.CharField(max_length=500)
    image_back = models.CharField(max_length=500)
    types = models.ManyToManyField(PokemonType, related_name='pokemonmodel')
    
    def __str__(self):
        return self.name