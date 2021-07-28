from django.db import models
from django.db import models

class Ad(models.Model):
    company_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.company_name} {self.phone_number}'