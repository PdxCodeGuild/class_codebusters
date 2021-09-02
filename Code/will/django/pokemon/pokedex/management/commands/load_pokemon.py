from django.core.management.base import BaseCommand
from pokedex.models import Pokemon, PokemonType
import json


class Command(BaseCommand):

    def handle(self, *args, **options):

        PokemonType.objects.all().delete()
        Pokemon.objects.all().delete()

        with open('pokemon.json', 'r') as file:
            allpokemon = json.loads(file.read())

        for poke in allpokemon['pokemon']:
            pokemon = Pokemon()
            pokemon.number = poke['number']
            pokemon.name = poke['name']
            pokemon.height = poke['height']
            pokemon.weight = poke['weight']
            pokemon.image_front = poke['image_front']
            pokemon.image_back = poke['image_back']
            pokemon.save()
            for type in poke['types']:
                newtype,created = PokemonType.objects.get_or_create(name = type)
                if created:
                    newtype.name = type
                    newtype.save()
                pokemon.types.add(newtype)

       