from shortener.models import ShortenedURL
from django.shortcuts import render, redirect
from django.http import HttpResponse
from string import ascii_letters, digits
from random import choice


def home_page(request):
    shortened_urls = ShortenedURL.objects.all().order_by('-visits')
    query_string = request.GET
    short_link = query_string.get('short_link', '')
    context = {
        'shortened_urls': shortened_urls,
        'short_link': short_link
    }
    return render(request, 'shortener/index.html', context)


def save(request):
    if request.method == "POST":
        form = request.POST
        code = ""
        char_bank = ascii_letters + digits
        for i in range(6):
            code += choice(char_bank)

        shortened_url = ShortenedURL()
        shortened_url.url = form['url']
        shortened_url.code = code
        shortened_url.visits = 0
        shortened_url.save()
    elif request.method == "GET":
        print("Nice try...")

    return redirect(f'../?short_link=home/{code}')


def redir(request, data):
    url_obj = ShortenedURL.objects.get(code=data)
    url_obj.visits += 1
    url_obj.save()
    return redirect(url_obj.url)
