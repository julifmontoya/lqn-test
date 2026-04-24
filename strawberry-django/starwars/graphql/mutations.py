# starwars/graphql/mutations.py
import strawberry
from typing import List, Optional
from starwars import services
from .types import CharacterType, FilmType, PlanetType


@strawberry.type
class Mutation:

    @strawberry.mutation
    def create_planet(self, name: str) -> PlanetType:
        return services.create_planet(name)

    @strawberry.mutation
    def create_film(
        self,
        title: str,
        opening_crawl: str,
        director: str,
        producers: str,
        planet_ids: Optional[List[int]] = None,
    ) -> FilmType:
        return services.create_film(
            title, opening_crawl, director, producers, planet_ids
        )

    @strawberry.mutation
    def create_character(
        self,
        name: str,
        film_ids: Optional[List[int]] = None,
    ) -> CharacterType:
        return services.create_character(name, film_ids)