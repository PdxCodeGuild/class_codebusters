from django.core.management.base import BaseCommand
from pokedex.models import Pokemon, PokemonType
import json

class Command(BaseCommand):

    def handle(self, *args, **options):

        Pokemon.objects.all().delete()
        PokemonType.objects.all().delete()

        # Load pokemon from file
        with open('pokemon.json', 'r') as file:
            pokemons = json.loads(file.read())
        
        # Add Pokemon Types
        types = []
        for poke in pokemons['pokemon']:
            for type in poke['types']:
                if type in types:
                    pass
                else:
                    types.append(type)
        
        for type in types:
            newtype = PokemonType()
            newtype.name = type
            newtype.save()

        # Add Pokemons
        for poke in pokemons['pokemon']:
            newpoke = Pokemon()
            newpoke.number = poke['number']
            newpoke.name = poke['name']
            newpoke.height = poke['height']
            newpoke.weight = poke['weight']
            newpoke.image_front = poke['image_front']
            newpoke.image_back = poke['image_back']
            newpoke.save()
            for type in poke['types']:
                t = PokemonType.objects.get(name=type)
                newpoke.types.add(t)

            newpoke.save()