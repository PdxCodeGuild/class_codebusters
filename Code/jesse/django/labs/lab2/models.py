from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    public = models.BooleanField()
    date_created = DateTimeField(auto_now_add=True)
    date_edited = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title