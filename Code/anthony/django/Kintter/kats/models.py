from django.db import models

# Create your models here.
class Cat(models.Model):
    url = models.URLField(unique=True)
    up_doots = models.IntegerField(default=0)
    down_doots = models.IntegerField(default=0)

    def __str__(self):
        return f"Cat #{self.id}"

    def get_doots(self):
        return self.up_doots - self.down_doots