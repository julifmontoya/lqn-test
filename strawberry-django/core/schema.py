# core/schema.py
import strawberry
from starwars.graphql.queries import Query
from starwars.graphql.mutations import Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)