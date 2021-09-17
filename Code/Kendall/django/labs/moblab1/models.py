from django.db import models

# Create your models here.


class ShortenedURL(models.Model):
    code = models.CharField(max_length=10)
    url = models.URLField()


def __str__(self):
    return f'{self.code} : {self.url}'
