from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.http import HttpResponse
from .models import BlogPost

# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request, 'lab2/register.html')
    elif request.method == 'POST':
        return HttpResponseRedirect(reverse('blog:profile'))

def login(request):
    if request.method == 'GET':
        return render(request, 'lab2/login.html')
    elif request.method == 'POST':
        return HttpResponseRedirect(reverse('blog:profile'))

@login_required
def profile(request):

    blogposts = BlogPost.objects.filter(user=request.user)
    print(blogposts)
    context = {
        'blogposts': blogposts
    }
    print(context)

    return render(request, 'lab2/profile.html', context)

@login_required
def create(request):
    
    print(request.POST)
    form = request.POST
    title = form['title']
    body = form['body']
    user = request.user
    if 'public' in form:
        public = True
    else:
        public = False

    # blogpost = BlogPost()
    # blogpost.title = title
    # blogpost.body = body
    # blogpost.user = user
    # blogpost.public = public

    blogpost = BlogPost(title=title, body=body, user=user, public=public)

    blogpost.save()

    return HttpResponseRedirect(reverse('blog:profile'))