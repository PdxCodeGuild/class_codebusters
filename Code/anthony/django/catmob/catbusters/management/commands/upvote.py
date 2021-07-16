from django.core.management.base import BaseCommand
from catbusters.models import Cat
import random

class Command(BaseCommand):

    def handle(self, *args, **options):
        # assign random 0-100 upvote and downvote
        cats = Cat.objects.all()

        for cat in cats:
            cat.up_votes = random.randint(1, 100)
            cat.down_votes = random.randint(1, 100)
            cat.total_votes = cat.get_total()
            cat.save()