from django.db import models

# Create your models here.


# Question
class Question(models.Model):
    question_text = models.CharField(max_length=150)

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
