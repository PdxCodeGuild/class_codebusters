from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, reverse
from django.http import HttpResponse
import requests
from .models import Cat


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

    # Save cat_url to database
    cat = Cat()
    cat.url = cat_url
    cat.save()

    return render(request, 'catbusters/index.html', context)


def all(request):
    cats = Cat.objects.all().order_by('-total_votes')

    context = {
        'cats': cats
    }

    return render(request, 'catbusters/all.html', context)

def up_vote(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    cat.up_votes += 1
    cat.total_votes = cat.get_total()
    cat.save()

    return HttpResponseRedirect(reverse('catbusters:all'))

def down_vote(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    cat.down_votes += 1
    cat.total_votes = cat.get_total()
    cat.save()

    return HttpResponseRedirect(reverse('catbusters:all'))