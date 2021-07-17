from django.contrib import admin
from . import models

admin.site.register(models.PokemonType)
admin.site.register(models.Pokemon)
