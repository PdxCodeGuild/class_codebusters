from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from . import secrets

import requests as fetch

from .models import Cat

# Create your views here.
def home(request):
    # Get Cat categories
    cat_url = 'https://api.thecatapi.com/v1/categories'
    response = fetch.get(cat_url, headers = {'x-api-key': secrets.api_key})
    cat_egories = response.json()

    # Random cat image url
    URL = 'https://api.thecatapi.com/v1/images/search'

    # If category specified in query params, get cat from that category
    if 'category' in request.GET:
        category = request.GET['category']
        valid = False
        for cat in cat_egories:
            if str(cat['id']) == category:
                valid = True
                break
        if valid:
            URL = 'https://api.thecatapi.com/v1/images/search?category_ids=' + category

    # Getting cat image url
    response = fetch.get(URL)
    data = response.json()
    cat_image = data[0]['url']

    cat = Cat(url=cat_image)
    cat.save()


    context = {
        'cat_image': cat_image,
        'cat_egories': cat_egories
    }

    return render(request, 'kats/index.html', context)


def get_cat(request):
    form = request.POST
    category = form['category']

    print(request.META['REMOTE_ADDR'])

    return HttpResponseRedirect(reverse('kats:home') + f'?category={category}')


def all_cats(request):
    cats = Cat.objects.all().order_by('-up_doots')
    context = {
        'cats': cats
    }

    return render(request, 'kats/view_all.html', context)


def vote_up(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    cat.up_doots += 1
    cat.save()
    return HttpResponseRedirect(reverse('kats:view_all'))

def vote_down(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    cat.down_doots += 1
    cat.save()
    return HttpResponseRedirect(reverse('kats:view_all'))