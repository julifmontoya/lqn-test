# starwars/tests/test_mutations.py
import json
from django.test import TestCase
from starwars.models import Planet, Film, Character


class MutationTests(TestCase):

    GRAPHQL_URL = "/graphql/"

    def execute(self, query, variables=None):
        return self.client.post(
            self.GRAPHQL_URL,
            data=json.dumps({
                "query": query,
                "variables": variables or {}
            }),
            content_type="application/json"
        )

    # Create Planet
    def test_create_planet(self):
        query = """
        mutation {
            createPlanet(name: "Tatooine") {
                id
                name
            }
        }
        """

        response = self.execute(query)
        data = response.json()

        self.assertIsNone(data.get("errors"))
        self.assertEqual(data["data"]["createPlanet"]["name"], "Tatooine")
        self.assertEqual(Planet.objects.count(), 1)

    # Create Film
    def test_create_film(self):
        planet = Planet.objects.create(name="Tatooine")

        query = f"""
        mutation {{
            createFilm(
                title: "A New Hope"
                openingCrawl: "Test crawl"
                director: "George Lucas"
                producers: "Lucasfilm"
                planetIds: [{planet.id}]
            ) {{
                id
                title
                planets {{
                    name
                }}
            }}
        }}
        """

        response = self.execute(query)
        data = response.json()

        self.assertIsNone(data.get("errors"))
        self.assertEqual(data["data"]["createFilm"]["title"], "A New Hope")
        self.assertEqual(
            data["data"]["createFilm"]["planets"][0]["name"],
            "Tatooine"
        )
        self.assertEqual(Film.objects.count(), 1)

    # Create Character
    def test_create_character(self):
        film = Film.objects.create(
            title="A New Hope",
            opening_crawl="...",
            director="George Lucas",
            producers="Lucasfilm"
        )

        query = f"""
        mutation {{
            createCharacter(
                name: "Luke Skywalker"
                filmIds: [{film.id}]
            ) {{
                id
                name
                films {{
                    title
                }}
            }}
        }}
        """

        response = self.execute(query)
        data = response.json()

        self.assertIsNone(data.get("errors"))
        self.assertEqual(data["data"]["createCharacter"]
                         ["name"], "Luke Skywalker")
        self.assertEqual(
            data["data"]["createCharacter"]["films"][0]["title"],
            "A New Hope"
        )
        self.assertEqual(Character.objects.count(), 1)
