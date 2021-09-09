from pokedex.models import Pokemon
from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon


def home(request):
    pokes = Pokemon.objects.all()

    context = {
        'pokes': pokes
    }

    return render(request, 'pokedex/index.html', context)


def all_pokes(request, name):
    poke = Pokemon.objects.get(name=name)

    context = {
        'poke': poke
    }

    return render(request, 'pokedex/all_pokes.html', context)
