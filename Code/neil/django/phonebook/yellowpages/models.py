from django.db import models

# Create your models here.


class Ad(models.Model):
    company_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.company_name
