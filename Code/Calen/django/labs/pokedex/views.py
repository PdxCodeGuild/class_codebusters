from django.shortcuts import render, get_object_or_404
from .models import Pokemon, PokemonType


# Create your views here.

def home(request):
    context = {
        'pokedex': Pokemon.objects.all(),
        'type_list': PokemonType.objects.all(), 
    }
    return render(request, 'pokedex/home.html', context)    


def details(request, number):
    number = str(int(number)+3)
    pokemon = get_object_or_404(Pokemon, id=number)

    context = {
        'pokemon' : pokemon
    } 
    return render(request, 'pokedex/details.html', context)




def type(request, type):
    type_lookup = get_object_or_404(PokemonType, name=type)
    type_pokemon = Pokemon.objects.filter(types=type_lookup)
    context = {
        'type' : type_lookup,
        'type_pokemon' : type_pokemon
    } 
    return render(request, 'pokedex/type.html', context)