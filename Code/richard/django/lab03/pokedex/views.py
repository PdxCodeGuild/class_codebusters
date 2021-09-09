from pokedex.models import Pokemon
from django.shortcuts import render

def home(request):
    pokemons = Pokemon.objects.all()
    context = {
        'pokemons':pokemons
    }
    return render(request, 'pokedex/index.html',context)

def details(request,poke_id):
    pokemon = Pokemon.objects.get(id = poke_id)
    context = {
        'pokemon':pokemon
    }
    return render(request, 'pokedex/details.html',context)
