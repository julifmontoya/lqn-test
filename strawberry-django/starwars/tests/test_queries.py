# starwars/tests/test_queries.py
import json
from django.test import TestCase
from starwars.models import Character


class TestQuery(TestCase):

    GRAPHQL_URL = "/graphql/"

    def execute(self, query):
        return self.client.post(
            self.GRAPHQL_URL,
            data=json.dumps({"query": query}),
            content_type="application/json",
        )

    def test_characters(self):
        Character.objects.create(name="Luke Skywalker")

        query = """
        query {
            characters {
                id
                name
            }
        }
        """

        response = self.execute(query)
        data = response.json()

        self.assertIsNone(data.get("errors"))
        self.assertEqual(len(data["data"]["characters"]), 1)
        self.assertEqual(
            data["data"]["characters"][0]["name"],
            "Luke Skywalker"
        )