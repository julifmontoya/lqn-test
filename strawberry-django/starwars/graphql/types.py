# starwars/graphql/types.py
import strawberry_django
from typing import List
from strawberry import auto
from starwars.models import Character, Film, Planet


@strawberry_django.type(Planet)
class PlanetType:
    id: auto
    name: auto


@strawberry_django.type(Film)
class FilmType:
    id: auto
    title: auto
    opening_crawl: auto
    director: auto
    producers: auto
    planets: List["PlanetType"]


@strawberry_django.type(Character)
class CharacterType:
    id: auto
    name: auto
    films: List["FilmType"]