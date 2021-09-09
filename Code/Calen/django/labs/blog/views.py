from django.db.models.fields import DateField, DateTimeField
from blog.models import BlogPost
from typing import ContextManager
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    username = request.user.username

    public_posts = BlogPost.objects.all()

    context = {
        'public_posts' : public_posts,
    }

    return render(request, 'blog/index.html', context)


# redirect to profile after
def register(request):
    username = request.user.username

    if request.method == 'GET':
        return render(request, 'blog/register.html')

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

        return HttpResponseRedirect(reverse('blog:home'))


# redirect to profile after
def login_page(request):
    username = request.user.username

    if request.method == 'GET':
        return render(request, 'blog/Login.html')
    
    elif request.method == 'POST':
        form = request.POST
        username = form['username']
        password = form['password']

        # auth time
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)


        return HttpResponseRedirect(reverse('blog:home'))




# must be protected for login only. 
# part one shows a welcome message for now.
@login_required
def profile_page(request):
    username = request.user.username
    user = get_object_or_404(User, username=username)


    context= {
        'user' : user,
    }

    return render(request, 'blog/profile.html', context)



@login_required
def create(request):
    username = request.user.username
    user = get_object_or_404(User, username=username)

    if request.method == 'GET':
        context= {
            'user' : user,
        }

        return render(request, 'blog/create.html', context)



    elif request.method == 'POST':
        form = request.POST
        title = form['title']
        body = form['body']

        public = form['public']
        if public == 'on':
            public = True
        else:
            public = False

        new_post = BlogPost()
        new_post.title = title
        new_post.body = body
        new_post.user = request.user
        new_post.public = public
        new_post.date_created = DateTimeField(auto_now_add=True)
        new_post.date_edited = DateTimeField(auto_now=True)
        new_post.photo = form['photo']
        new_post.save()
        return HttpResponseRedirect(reverse('blog:profile'))



def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:home'))

