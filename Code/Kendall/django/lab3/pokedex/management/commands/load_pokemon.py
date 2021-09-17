from django.core.management.base import BaseCommand
import json

from pokedex.models import Pokemon, PokemonType


class Command(BaseCommand):

    def handle(self, *args, **options):
        # delete all records to start with clean slate
        PokemonType.objects.all().delete()
        Pokemon.objects.all().delete()
        # open json file
        f = open('pokemon.json',)
        contents = json.load(f)

        # save each category to the database
        for content in contents['pokemon']:
            pokemontype = PokemonType()
            pokemon = Pokemon()

            pokemontype.name = content['types']
            pokemontype.save()

            # print(content['weight'])

            pokemon.number = content['number']
            pokemon.name = content['name']
            pokemon.height = content['height']
            pokemon.weight = content['weight']
            pokemon.image_front = content['image_front']
            pokemon.image_back = content['image_back']
            pokemon.save()

        f.close()

        # poketypes.save()
        # pokemons.save()
