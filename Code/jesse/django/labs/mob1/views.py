from mob1.models import ShortenedURL
from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
import string

# Create your views here.

def home(request):

    shortened_urls = ShortenedURL.objects.all()

    context = {
        'shortened_urls': shortened_urls
    }

    return render(request, 'mob1/index.html', context)

def save(request):

    char = string.ascii_letters + string.digits
    code = ''

    for i in range(6):
        code += random.choice(char)

    url = ShortenedURL()
    form = request.POST
    url.code = code
    url.url = form['url']
    url.counter = 0
    url.save()

    return redirect('../')

def redir(request, data):

    shortened_urls = ShortenedURL.objects.filter(code=data)
    print(list(shortened_urls))
    if len(shortened_urls) > 0:
        shortened_urls[0].counter += 1
        shortened_urls[0].save()
        return redirect(shortened_urls[0].url)

    return HttpResponse('That code does not exist.')