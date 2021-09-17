from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import BlogPost
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    blogs = BlogPost.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/index.html', context)


def register(request):
    print('METHOD', request.method)
    if request.method == "GET":
        return render(request, 'blog/register.html')
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

        return render(request, 'blog/profile.html')


def user_login(request):
    if request.method == 'GET':
        return render(request, 'blog/login.html')
    elif request.method == 'POST':
        form = request.POST
        username = form['username']
        password = form['password']

        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)

        return HttpResponseRedirect(reverse('blog:home'))


@login_required
def profile(request):
    pass


@login_required
def create(request):
    if request.method == 'GET':
        return render(request, 'blog/create.html')
    elif request.method == 'POST':
        return render(request, 'blog/register.html')
