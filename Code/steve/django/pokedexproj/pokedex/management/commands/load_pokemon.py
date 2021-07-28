from django.core.management.base import BaseCommand
from pokedex.models import PokemonType, Pokemon
import json


class Command(BaseCommand):

    def handle(self, *args, **options):

        Pokemon.objects.all().delete()

        with open('pokemon.json', 'r') as file:
            pokemons = json.loads(file.read())

        for pokemon in pokemons['pokemon']:
            poke = Pokemon()
            poke.number = pokemon['number']
            poke.name = pokemon['name']
            poke.height = pokemon['height']
            poke.weight = pokemon['weight']
            poke.image_front = pokemon['image_front']
            poke.image_back = pokemon['image_back']
            poke.save()
            for type in pokemon['types']:
                p_type = PokemonType(name=type)
                p_type.save()
                poke.types.add(p_type)
            poke.save()
