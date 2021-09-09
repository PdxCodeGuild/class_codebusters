from typing import ChainMap
from django.db import models
from django.db.models.fields import BooleanField, CharField, DateTimeCheckMixin, DateTimeField
from django.db.models.fields.related import ForeignKey, ForeignObject
from django.contrib.auth.models import User


# Create your models here.


class BlogPost(models.Model):
    title = CharField(max_length=250)
    body = CharField(max_length=600)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts')
    public = BooleanField(default=False)
    date_created = DateTimeField(auto_now_add=True)
    date_edited = DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.title}, Authored by {self.user}'

