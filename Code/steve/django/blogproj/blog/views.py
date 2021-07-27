from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import BlogPost


def home_page(request):
    return render(request, 'blog/index.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'blog/register.html')
    elif request.method == 'POST':
        # get data from form
        form = request.POST
        username = form['username']
        password = form['password']
        email = form['email']
        first_name = form['first_name']
        last_name = form['last_name']

        # create user - username, email, password order matters
        user = User.objects.create_user(
            username, email, password, first_name=first_name, last_name=last_name)

        login(request, user)

        return HttpResponseRedirect(reverse('blog:profile'))


@login_required
def profile(request):
    blogs = BlogPost.objects.filter(user=request.user)

    context = {
        "blogs": blogs
    }

    return render(request, 'blog/profile.html', context)


def login_user(request):
    # user visits page
    if request.method == 'GET':
        return render(request, 'blog/login.html')
    elif request.method == 'POST':
        form = request.POST
        username = form['username']
        password = form['password']

        # authenticate user
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)

    return HttpResponseRedirect(reverse('blog:profile'))


def logout_user(request):
    logout(request)

    return HttpResponseRedirect(reverse('blog:home'))


@login_required
def create_blog(request):
    if request.method == 'GET':
        return render(request, 'blog/create.html')
    elif request.method == 'POST':
        form = request.POST
        title = form['title']
        body = form['body']

        blog = BlogPost()
        blog.title = title
        blog.body = body
        blog.user = request.user

        # title = request.POST.get('title')
        # body = request.POST.get('body')

        # blog = BlogPost.objects.create(
        #     title=title, body=body, user=request.user)

        blog.save()

        return render(request, 'blog/index.html')
