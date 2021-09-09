from django.shortcuts import render
from django.http import HttpResponse
from .models import Ad
# Create your views here.

def home_page(request):
    
    ads = Ad.objects.all()

    context = {
        'ads': ads
    }

    return render(request, 'yellowpages/index.html', context)