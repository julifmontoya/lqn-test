# starwars/services.py
from typing import List, Optional
from .models import Character, Film, Planet


# 🔹 Queries
def get_characters(name: Optional[str] = None) -> List[Character]:
    qs = Character.objects.all()
    if name:
        qs = qs.filter(name__icontains=name)
    return qs


def get_films() -> List[Film]:
    return Film.objects.all()


def get_planets() -> List[Planet]:
    return Planet.objects.all()


# 🔹 Mutations
def create_planet(name: str) -> Planet:
    return Planet.objects.create(name=name)


def create_film(
    title: str,
    opening_crawl: str,
    director: str,
    producers: str,
    planet_ids: Optional[List[int]] = None,
) -> Film:
    film = Film.objects.create(
        title=title,
        opening_crawl=opening_crawl,
        director=director,
        producers=producers,
    )

    if planet_ids:
        film.planets.set(Planet.objects.filter(id__in=planet_ids))

    return film


def create_character(
    name: str,
    film_ids: Optional[List[int]] = None,
) -> Character:
    character = Character.objects.create(name=name)

    if film_ids:
        character.films.set(Film.objects.filter(id__in=film_ids))

    return character