from typing import Container
from django import http
from django.db.models.fields import EmailField
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Ad
# Create your views here.

def home_page(request):

    ads = Ad.objects.all()

    context = {
        'ads': ads
    }

    return render(request, 'yellowpages/index.html', context)