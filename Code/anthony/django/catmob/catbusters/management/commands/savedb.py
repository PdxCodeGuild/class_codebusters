from django.core.management.base import BaseCommand
from catbusters.models import Cat
import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        # List of dictionaries
        # each cat is a dictionary

        cats = Cat.objects.all()

        output = []
        for cat in cats:
            cat_dict = {
                'id': cat.id,
                'url': cat.url
            }
            output.append(cat_dict)

        with open('backup.json', 'w') as file:
            file.write(json.dumps(output))