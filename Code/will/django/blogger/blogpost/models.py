from django.db import models


class Blogpost(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=50)
    public = models.BooleanField(null=True, blank=True)
    date_created = models.DateTimeField(null=True, blank=True)
    date_edited = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.title