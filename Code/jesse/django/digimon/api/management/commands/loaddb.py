from django.core.management.base import BaseCommand
import requests
from api.models import Level, Digimon

class Command(BaseCommand):

    def handle(self, *args, **options):
        response = requests.get('https://digimon-api.vercel.app/api/digimon')
        data = response.json()

        for mon in data:
            level, _ = Level.objects.get_or_create(evolution=mon['level'])
            digimon = Digimon()
            digimon.name = mon['name']
            digimon.img = mon['img']
            digimon.level = level
            digimon.save()