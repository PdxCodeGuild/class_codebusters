from django.db import models

# Create your models here.


class ShortenedURL(models.Model):
    code = models.CharField(max_length=8, unique=True)
    url = models.URLField()
    visits = models.IntegerField()

    def __str__(self):
        # AI Generated 🤖
        return self.code
