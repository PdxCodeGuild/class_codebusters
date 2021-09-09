from typing import ContextManager
from django import http
from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from .models import Question, Choice
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'polls/index.html', context)

@login_required
def vote(request, choice_id):
    # choice = Choice.objects.get(id=choice_id)
    choice = get_object_or_404(Choice, id=choice_id)
    choice.votes += 1
    choice.save()
    context = {
        'question' : choice.question
    }
    return render(request, 'polls/results.html', context)


@login_required
def generate_choices(request):
    form = request.POST
    text = form['question_text']
    num_choices = form['num_choices']

    question = Question()
    question.question_text = text
    question.user = request.user
    question.save()

    context = {
        'choices': list(range(int(num_choices))),
        'question_id': question.id,
    }

    return render(request, 'polls/choices.html', context)


@login_required
def add_choices(request):
    form = request.POST
    question = get_object_or_404(Question, id=form('question_id'))
    
    for key in form:
        if key.startswith('choice'):
            new_choice = Choice()
            new_choice.choice_text = form[key]
            new_choice.question = question
            new_choice.save()


    
    
    return HttpResponseRedirect(reverse('polls:home'))

def signup(request):
    if request.method == 'GET':
        return render(request, 'polls/signup.html')

    elif request.method == 'POST':
        form = request.POST
        user = User.objects.create_user(
            form['username'], 
            form['email'], 
            form['password'], 
            first_name=form['first_name'], 
            last_name=form['last_name'],
            )
        
        login(request, user)

        return HttpResponseRedirect(reverse('polls:home'))

def login_user(request):
    if request.method == 'GET':
        return render(request, 'polls/login.html')

    elif request.method == 'POST':
        form = request.POST
        username = form['username']
        password = form['password']

        # auth time bb
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)


        return HttpResponseRedirect(reverse('polls:home'))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('polls:home'))
    

def user_polls(request, username):

    user = get_object_or_404(User, username=username)

    context= {
        'user' : user,
    }
    return render(request, 'polls/user_polls.html', context)
