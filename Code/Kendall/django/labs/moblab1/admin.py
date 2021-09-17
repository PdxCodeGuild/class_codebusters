from django.contrib import admin

# Register your models here.
from .models import ShortenedURL
admin.site.register(ShortenedURL)
