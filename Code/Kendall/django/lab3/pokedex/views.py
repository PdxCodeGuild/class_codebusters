from django.shortcuts import render
from django.http import HttpResponse
from .models import PokemonType, Pokemon

# Create your views here.


def home(request):
    pokemons = Pokemon.objects.all()
    context = {
        'pokemons': pokemons
    }
    return render(request, 'pokedex/index.html', context)
