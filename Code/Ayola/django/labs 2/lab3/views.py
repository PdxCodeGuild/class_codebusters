from django.http import request
from django.shortcuts import render
from . import pokemanager
from . import models

# Create your views here.
def pokelist(request):
    pokemons = models.Pokemon.objects.all()
    context = dict()
    context['pokemons'] = pokemons
    return render(request,"poke.html",context)


def details(request):
    number = request.POST.get("number")
    pokemon = models.Pokemon.objects.get(number=number)
    context = dict()
    context['poke'] = pokemon
    return render(request,"details.html",context)