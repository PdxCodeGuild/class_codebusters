from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

# questions
class Question(models.Model):
    question_text = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='questions')
    def __str__(self):
        return self.question_text

# choice
class Choice(models.Model):
    choice_text = models.CharField(max_length=75)

    votes = models.IntegerField(default=0)

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')

    def __str__(self):
        return self.choice_text



choice = Choice()
print(choice)
str(choice)