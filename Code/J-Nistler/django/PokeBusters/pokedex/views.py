from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Pokemon, PokemonType
import json

# Create your views here.
def home (request):

    return render(request, 'pokedex/index.html')

def all_pokemon (request):
    pokemons = list(Pokemon.objects.all().values())

    return JsonResponse(pokemons, safe=False)