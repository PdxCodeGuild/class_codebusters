from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Ad

def home_page(request):
    ads = Ad.objects.all()
    context = {
        'ads' : ads
    }
    return render(request,'yellowpages/index.html', context)