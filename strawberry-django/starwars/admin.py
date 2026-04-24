# starwars/admin.py
from django.contrib import admin
from .models import Character, Film, Planet


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "director")
    filter_horizontal = ("planets",)


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    filter_horizontal = ("films",)