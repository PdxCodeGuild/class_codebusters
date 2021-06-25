from django.http.response import HttpResponse
from django.shortcuts import redirect, render
# from .models import Yellowpages

def home_page(request):
    return render(request, 'yellowpages/index.html')