from django.core.management.base import BaseCommand
from catbusters.models import Cat
import privates
import requests
import json

class Command(BaseCommand):

    def handle(self, *args, **options):

        Cat.objects.all().delete()

        with open('backup.json', 'r') as file:
            cats = json.loads(file.read())

        for cat in cats:
            kitten = Cat()
            kitten.id = cat['id']
            kitten.url = cat['url']
            kitten.save()

        # response = requests.get('https://api.thecatapi.com/v1/images/search?limit=100', headers={'x-api-key': privates.API_KEY})

        # cats = response.json()
        # for index, cat  in enumerate(cats):

        #     try:
        #         kat = Cat()
        #         kat.id = index + 1
        #         kat.url = cat['url']
        #         kat.save()
        #     except:
        #         continue
