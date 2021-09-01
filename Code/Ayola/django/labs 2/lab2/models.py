from django.db import models

# Create your models here.
class User(models.Model):

    email = models.CharField(max_length= 100, primary_key=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=200)

class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    body  = models.TextField(max_length=1000)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    public = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)