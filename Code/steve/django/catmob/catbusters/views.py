from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import requests
from .secrets import api_key


def home(request):
    cat_dict = (requests.get(
        'https://api.thecatapi.com/v1/images/search')).json()[0]

    cat_egories = (requests.get(
        'https://api.thecatapi.com/v1/categories')).json()

    cat_url = cat_dict['url']

    context = {
        'cat_url': cat_url,
        'cat_egories': cat_egories,
    }

    print(cat_egories)
    return render(request, 'catbusters/index.html', context)
