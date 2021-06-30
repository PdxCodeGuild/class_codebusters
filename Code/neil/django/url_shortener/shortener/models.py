from django.db import models
from django.db.models.fields import CharField, URLField, IntegerField

# Create your models here.


class ShortenedURL(models.Model):
    code = models.CharField(max_length=8)
    url = models.URLField()
    views = models.IntegerField(default=0)
