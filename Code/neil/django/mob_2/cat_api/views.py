from django.http.response import HttpResponseRedirect
from django.shortcuts import render,  reverse
from django.http import HttpResponse
import requests

# Create your views here.


def home(request):
    # cats = requests.get('https://api.thecatapi.com/v1/images/search',
    #                     headers={'accept': 'application/json'})

    # # for cat in cats:
    # #     pic_url = cat['url']
    # #     print(pic_url)

    # context = {
    #     'cats': cats.json()
    # }

    # print(context)
    # if request.method == 'GET':
    categories = requests.get('https://api.thecatapi.com/v1/categories',
                              headers={'accept': 'application/json'})

    context = {
        'categories': categories.json()
    }

    return render(request, 'cat_api/index.html', context)

    # elif request.method == 'POST':
    #     form = request.POST

    #     return render(request, 'cat_api/index.html', context)


def category(request):
    form = request.POST
    print(form['category'])
    categories = requests.get(f'https://api.thecatapi.com/v1/images/search?category_ids={form["category"]}',
                              headers={'accept': 'application/json'})

    context = {
        'categories': categories.json()
    }

    return render(request, 'cat_api/category.html', context)


def random(request):
    return HttpResponseRedirect(reverse('cat_api:home'))
