# starwars/graphql/queries.py
import strawberry
from typing import List, Optional
from starwars import services
from .types import CharacterType, FilmType, PlanetType


@strawberry.type
class Query:

    # 🔹 Characters
    @strawberry.field
    def characters(self, name: Optional[str] = None) -> List[CharacterType]:
        return services.get_characters(name)

    # 🔹 Films
    @strawberry.field
    def films(self) -> List[FilmType]:
        return services.get_films()

    # 🔹 Planets
    @strawberry.field
    def planets(self) -> List[PlanetType]:
        return services.get_planets()