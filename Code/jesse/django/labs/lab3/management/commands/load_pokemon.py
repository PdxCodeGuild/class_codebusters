from django.core.management.base import BaseCommand
from lab3.models import PokemonType, Pokemon
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        Pokemon.objects.all().delete()
        PokemonType.objects.all().delete()
        
        # try:
        #     f = open('pokemon.json')
        #     pokedex = json.loads(f.read())
        # except (IOError, OSError) as e:
        #     print(e)
        # finally:
        #     f.close()
            
        with open('pokemon.json', 'r') as f:
            pokedex = json.loads(f.read())

        for entry in pokedex['pokemon']:
            pokemon = Pokemon()
            pokemon.number = entry['number']
            pokemon.name = entry['name']
            pokemon.height = entry['height']
            pokemon.weight = entry['weight']
            pokemon.image_front = entry['image_front']
            pokemon.image_back = entry['image_back']
            pokemon.save()
            for poketype in entry['types']:
                pokemon_type, _ = PokemonType.objects.get_or_create(name=poketype)
                pokemon_type.save()
                pokemon.types.add(pokemon_type)
            pokemon.save()