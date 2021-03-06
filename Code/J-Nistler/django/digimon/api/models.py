from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.
class Level (models.Model):
    evolution = models.CharField(max_length=15) 

    def __str__(self):
        return self.evolution


class Digimon (models.Model):
    name = models.CharField(max_length=15)
    img = models.URLField()
    level = models.ForeignKey(Level, on_delete=PROTECT, related_name='digimon')

    def __str__(self):
        return self.name
