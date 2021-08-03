from django.db import models

# Create your models here.
class TodoPriority(models.Model):
    text = models.CharField(max_length=20)
    # Value of 1 is most important, 3 least important
    value = models.IntegerField(default=3)

    def __str__(self):
        return self.text


class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    created_date = models.DateField(auto_now_add=True)
    completed_date = models.DateField(blank=True, null=True)
    priority = models.ForeignKey(TodoPriority, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.priority} - {self.text}'