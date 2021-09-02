from django.shortcuts import render
from .models import Pokemon


def home(request):
    pokemons = Pokemon.objects.all()
    context = {
        'pokemons': pokemons
    }
    return render(request, 'pokedex/index.html', context)

def info(request,poke_id):
    pokemon = Pokemon.objects.get(id = poke_id)
    context = {
        'pokemon': pokemon
    }
    return render(request, 'pokedex/info.html', context)

