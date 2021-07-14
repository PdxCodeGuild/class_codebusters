from django.db import models

# Create your models here.


class ItemPriority(models.Model):
    text = models.CharField(max_length=10)
    value = models.IntegerField()
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.text


class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    priority = models.ForeignKey(ItemPriority, on_delete=models.PROTECT, related_name='todo_items')

    def __str__(self):
        #  (high) - Feed the dogs
        return f'({self.priority.text}) - {self.title}'
