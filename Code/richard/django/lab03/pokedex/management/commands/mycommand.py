from django.core.management.base import BaseCommand
from pokedex.models import Pokemon, PokemonType
import json


class Command(BaseCommand):

    def handle(self, *args, **options):

        PokemonType.objects.all().delete()
        Pokemon.objects.all().delete()
        

        with open('pokemon.json') as file:
            allPoke = json.loads(file.read())


        for poke in allPoke['pokemon']:
            pokemon = Pokemon()
            poketypes = []
            for typ in poke['types']:
                try:
                    PokemonType.objects.get(name = typ)
                except:
                    typ1 = PokemonType(name = typ)
                    typ1.save()
                poketypes.append(typ1)

            pokemon.number = poke['number']
            pokemon.name = poke['name']
            pokemon.height = poke['height']
            pokemon.weight = poke['weight']
            pokemon.image_front = poke['image_front']
            pokemon.image_back = poke['image_back']
            pokemon.save()
            for poketype in poketypes:
                pokemon.types.add(poketype)