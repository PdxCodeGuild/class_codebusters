from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
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
    choice_id = 3 if choice_id == 4 else choice_id

    choice = get_object_or_404(Choice, id=choice_id)
    choice.votes += 1
    choice.save()

    context = {
        'question': choice.question
    }
    return render(request, 'polls/results.html', context)


@login_required
def generate_choices(request):
    form = request.POST
    text = form['question_text']
    num_choice = form['num_choices']

    question = Question()
    question.question_text = text
    question.user = request.user
    question.save()

    num_choice = list(range(int(num_choice)))

    context = {
        'choices': num_choice,
        'question': question,
    }

    return render(request, 'polls/choices.html', context)


@login_required
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


def signup(request):
    print('METHOD', request.method)
    if request.method == "GET":
        return render(request, 'polls/signup.html')
    elif request.method == "POST":
        print('FORM', request.POST)
        form = request.POST
        username = form['username']
        password = form['password']
        email = form['email']
        first_name = form['first_name']
        last_name = form['last_name']
        user = User.objects.create_user(
            username, email, password, first_name=first_name, last_name=last_name)

        login(request, user)

        return HttpResponseRedirect(reverse('polls:home'))


def login_user(request):
    if request.method == 'GET':
        return render(request, 'polls/login.html')
    elif request.method == 'POST':
        form = request.POST
        username = form['username']
        password = form['password']

        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)

        return HttpResponseRedirect(reverse('polls:home'))


def logout_user(request):
    logout(request)

    return HttpResponseRedirect(reverse('polls:home'))


def user_polls(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user': user
    }
    return render(request, 'polls/user_polls.html', context)
