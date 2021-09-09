from django.db import models

class Tasks(models.Model):
    text = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.text}'