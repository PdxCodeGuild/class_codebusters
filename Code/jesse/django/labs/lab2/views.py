from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def register(request):
    return HttpResponse('hello world!')

def login(request):
    return HttpResponse('hello world!')

def profile(request):
    return HttpResponse('hello world!')