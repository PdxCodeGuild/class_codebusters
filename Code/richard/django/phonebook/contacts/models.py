from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length = 50, null=True, blank=True)
    last_name = models.CharField(max_length = 50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField()
    address = models.CharField(max_length=100, null=True, blank=True)
    is_cool = models.BooleanField()
    def __str__(self):
        return f'{self.email}'