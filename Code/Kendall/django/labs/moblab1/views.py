from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('OK!')


def save(request):
    return HttpResponse('OK!')


def redirect(request, code):
    return HttpResponse(f'{code}')
