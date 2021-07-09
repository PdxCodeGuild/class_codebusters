from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blog/index.html')

def register(request):
    if request.method == "GET":
        return render(request, 'blog/register.html')
    elif request.method == "POST":
        print('FORM', request.POST)

        # Get data from our form
        form = request.POST
        username = form['username']
        password = form['password']
        email = form['email']
        first_name = form['first_name']
        last_name = form['last_name']

        # Create user. username, email, password.
        user = User.objects.create_user(
            username, email, password, first_name=first_name, last_name=last_name)

        login(request, user)

        return HttpResponseRedirect(reverse('blog:profile', args=[request.user.username]))

def login_user(request):
    # User visits page
    if request.method == "GET":
        return render(request, 'blog/login.html')
    # User submits form
    elif request.method == "POST":
        print('FORM', request.POST)
        # Get form data
        form = request.POST
        username = form['username']
        password = form['password']

        # Authenticate User
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)

        return HttpResponseRedirect(reverse('blog:profile', args=[request.user.username]))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:home'))

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)

    context = {
        'user' : user
    }
    return render(request, 'blog/profile.html', context)

