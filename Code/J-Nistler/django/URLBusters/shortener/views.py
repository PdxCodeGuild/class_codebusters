from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ShortenedURL
from string import ascii_letters, digits
from random import choice

# Create your views here.


def home_page(request):
    return render(request, 'shortener/index.html')


def save_url(request):
    shorturl = ShortenedURL()
    form = request.POST

    char_bank = ascii_letters + digits
    code = ''

    for i in range(8):
        code += choice(char_bank)

    shorturl.url = form['url']
    shorturl.code = code
    shorturl.save()

    new_url = f'localhost:8000/shortener/{code}'

    context = {
        'code': code,
    }

    return HttpResponse(new_url)

# search for contact


def search_url(request, my_code):
    url_obj = ShortenedURL.objects.get(code=my_code)
    url = url_obj.url
    url_obj.views += 1
    url_obj.save()

    return HttpResponseRedirect(url)