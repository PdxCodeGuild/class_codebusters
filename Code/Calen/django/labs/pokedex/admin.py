from django.contrib import admin

# Register your models here.

from .models import Pokemon, PokemonType

admin.site.register(Pokemon)
admin.site.register(PokemonType)