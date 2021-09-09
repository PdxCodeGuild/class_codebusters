from django.shortcuts import render
from .models import PokemonType, Pokemon
from django.http import HttpResponse

# Create your views here.
def home(request):
    pokedex = Pokemon.objects.all()
    context = {
        'pokedex': pokedex
    }
    return render(request, 'lab3/index.html', context)

def details(request, pokemon_name):
    pokemon = Pokemon.objects.get(name=pokemon_name)
    context = {
        'pokemon': pokemon
    }
    return render(request, 'lab3/details.html', context)