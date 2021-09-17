from django.db import models

# Create your models here.


class ShortenedURL(models.Model):
    code = models.CharField(max_length=8)
    url = models.URLField()
    visits = models.IntegerField(default=0)

    def __str__(self):
        return self.code
