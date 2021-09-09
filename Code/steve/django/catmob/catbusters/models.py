from django.db import models

# Create your models here.
class Cat(models.Model):
    url = models.URLField(unique=True)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

    def get_total(self):
        return self.up_votes - self.down_votes