from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.http import HttpResponse

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
    return render(request, 'lab2/profile.html')