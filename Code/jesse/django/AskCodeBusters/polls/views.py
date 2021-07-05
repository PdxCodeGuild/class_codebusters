from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from .models import Question, Choice

# Create your views here.
def home(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'polls/index.html', context)

def vote(request, choice_id):
    choice_id = 3 if choice_id == 4 else choice_id
    # choice = Choice.objects.get(id=choice_id)
    choice = get_object_or_404(Choice, id=choice_id)
    choice.votes += 1
    choice.save()
    context = {
        'question': choice.question
    }
    return render(request, 'polls/results.html', context)

def generate_choices(request):
    form = request.POST
    text = form['question_text']
    num_choice = form['num_choice']
    
    question = Question()
    question.question_text = text
    question.save()

    num_choice = list(range(int(num_choice)))

    context = {
        'choices': num_choice,
        'question': question
    }

    return render(request, 'polls/choices.html', context)

def add_choices(request):
    form = request.POST
    question = get_object_or_404(Question, id=form['question_id'])

    for key in form:
        if key.startswith('choice'):
            new_choice = Choice()
            new_choice.choice_text = form[key]
            new_choice.question = question
            new_choice.save()

    return HttpResponseRedirect(reverse('polls:home'))