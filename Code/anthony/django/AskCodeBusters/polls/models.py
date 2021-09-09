from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# models.CASCADE = delete
# models.PROTECT = prevent deletion

# q = Question()
# q.user

# user = User()
# user.questions


# Question
class Question(models.Model):
    question_text = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="questions")

    def __str__(self):
        return self.question_text


# Choice
class Choice(models.Model):
    choice_text = models.CharField(max_length=75)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="choices")

    def __str__(self):
        return self.choice_text


# choice = Choice
# choice.question

# question = Question()
# question.choices
