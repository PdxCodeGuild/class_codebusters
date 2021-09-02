from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Blogpost


def home(request):
    context = {
        'blogposts': 'blogposts'
    }
    return render(request, 'blogpost/index.html', context)


def register(request):
    print(request.method)
    if request.method == "GET":
        return render(request, 'blogpost/register.html')
    elif request.method == "POST":
        print(request.POST)

        form = request.POST
        username = form['username']
        password = form['password']
        email = form['email']
        first_name = form['first_name']
        last_name = form['last_name']

        user = User.objects.create_user(
            username, email, password, first_name=first_name, last_name=last_name)

        login(request, user)

        return HttpResponseRedirect(reverse('blogpost:profile'))


def login_user(request):

    if request.method == "GET":
        return render(request, 'blogpost/login.html')

    elif request.method == "POST":
        print('FORM', request.POST)
        form = request.POST
        username = form['username']
        password = form['password']

        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)

        return HttpResponseRedirect(reverse('blogpost:profile'))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('blogpost:home'))


def profile(request):
    return render(request, 'blogpost/profile.html')


def create(request):

    if request.method == "GET":
        return render(request, 'blogpost/create.html')

    elif request.method == "POST":
   
        posts = Blogpost()
        print(request.POST['title'])
        form = request.POST
        posts.title = form['title']

        context = {
            'posts': posts
        }
        posts.save()
        return render(request, 'blogpost/create.html', context)
