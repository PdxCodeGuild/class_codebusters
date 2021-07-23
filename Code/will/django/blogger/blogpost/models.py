from django.db import models
from django.contrib.auth.models import User


class Blogpost(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=150)
    public = models.BooleanField(null=True, blank=True)
    date_created = models.DateTimeField(null=True, blank=True)
    date_edited = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)

