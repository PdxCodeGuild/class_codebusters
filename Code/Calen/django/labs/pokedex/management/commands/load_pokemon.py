from django.core.management.base import BaseCommand
import json
from pokedex.models import PokemonType, Pokemon
import os

class Command(BaseCommand):

    def handle(self, *args, **options):

        file = r'data.json'
        with open(file, 'r') as data:
            pokemon_data = json.loads(data.read())['pokemon']
            
            for creature in pokemon_data:
                newbie = Pokemon()

                newbie.number = creature['number']
                newbie.name = creature['name']
                newbie.height = creature['height']
                newbie.weight = creature['weight']
                newbie.image_front = creature['image_front']
                newbie.image_back = creature['image_back']
                newbie.save()
                for type in creature['types']:  
                    type, _ = PokemonType.objects.get_or_create(name = type)
                    newbie.types.add(type)
                newbie.save()
                




