from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import BlogPost


def home(request):
    return render(request, 'blog/index.html')

@login_required
def profile(request):
    return render(request, 'blog/profile.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'blog/register.html')
    elif request.method == 'POST':
        form = request.POST
        user = User.objects.create_user(
            form['username'],
            form['email'],
            form['password'],
            first_name = form['first_name'],
            last_name = form['last_name']
        )
        login(request, user)
        return HttpResponseRedirect(reverse('blog:profile'))

def login_user(request):
    if request.method == "GET":
        return render(request, 'blog/login_user.html')
    elif request.method == "POST":
        form = request.POST
        user = authenticate(
            request, 
            username=form['username'], 
            password=form['password']
        )
        if user != None:
            login(request, user)
            return HttpResponseRedirect(reverse('blog:profile'))
        return HttpResponseRedirect(reverse('blog:home'))

def create(request):
    if request.method == 'GET':
        return render(request, 'blog/create.html')
    elif request.method == 'POST':
        form = request.POST
        post = BlogPost()
        post.title = form['title']
        post.body = form['body']
        post.user = request.user
        post.public = form['public']
        post.save()
        return HttpResponseRedirect(reverse('blog:profile'))

def edit(request, blogpost_id):
    post = BlogPost.objects.get(id=blogpost_id)
    if request.method == 'GET':
        context = {
            'post':post
        }
        return render(request, 'blog/edit.html',context)
    elif request.method == 'POST':
        if request.user == post.user:
            form = request.POST
            post.title = form['title']
            post.body = form['body']
            post.user = request.user
            post.public = form['public']
            post.save()
            return HttpResponseRedirect(reverse('blog:profile'))
        else:
            return HttpResponseRedirect(reverse('blog:profile'))

