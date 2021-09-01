from django.http import request
from django.shortcuts import render, redirect
from . import models
email = ""
password = ""
user = ""

def login(request):
    context = dict()
    context['failed'] = False
    return render(request,"login.html")

def add_user(request):
    return render(request,"register.html")


def sign_up(request):
    global user
    name = request.POST.get("name")
    email = request.POST.get("email")
    password = request.POST.get("password")
    new_user = models.User.objects.create(email=email,name=name,password=password)
    new_user.save()
    user = new_user
    email = user.email
    password = user.password
    return redirect("profile")


# Create your views here.
def profile(request):
    global user, email,password

    if request.POST.get("email") == None:
         email = user.email
         password = user.password
         print(2)
    
    elif request.POST.get("email") != "":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(1)


    context = dict()
    
    #try:
    print(email)
    print(password)
    user = models.User.objects.get(email=email,password=password)
    try:
        posts = models.BlogPost.objects.filter(user=user)
    except:
        posts = []
    context['posts'] = posts
    return render(request,"profile.html",context=context)

    #except:
    #    context['failed'] = True
    #    return render(request,"login.html",context=context)


    

def add_post(request):
    body = request.POST.get("text")
    title = request.POST.get("title")
    if request.POST.get("public") == "on":
        public = True
    else:
        public = False
    print(request.POST)
    post = models.BlogPost.objects.create(user=user,body=body,title=title,public=public)
    post.save()
    return redirect("profile")
