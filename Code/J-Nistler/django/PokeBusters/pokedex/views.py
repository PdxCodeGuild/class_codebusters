from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Pokemon, PokemonType
import json

# Create your views here.
def home (request):
    pokemons = Pokemon.objects.all()

    context = {
        'pokemons' : json.dumps(pokemons)
    }

    return render(request, 'pokedex/index.html', context)