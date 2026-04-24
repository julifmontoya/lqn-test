# Star Wars GraphQL API (Django + Graphene)
## Overview
This project is a **GraphQL API built with Django** that allows users to explore the Star Wars universe.

You can:
* List all characters
* Filter characters by name
* View the films each character appears in
* View film details (opening crawl, director, producers, planets)
* Create characters, films, and planets

---
## Project Structure

```
api/
├── starwars/
│   ├── models.py
│   ├── services.py
│   ├── graphql/
│   │   ├── types.py
│   │   ├── queries.py
│   │   ├── mutations.py
│   ├── tests/
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── schema.py
├── manage.py
```

---
## Architecture Notes

* **Domain-driven structure**: all Star Wars logic is inside the `starwars` app
* **Service layer**: handles business logic and database operations
* **GraphQL layer**: separated into `types`, `queries`, and `mutations`
* **Optimized queries**: uses `prefetch_related` to avoid N+1 issues

---

## Tech Stack
* Python
* Django
* Strawberry GraphQL (strawberry-graphql + strawberry-graphql-django)
* SQLite (default)

---

## Getting Started
```bash
git clone <repo-url>
cd api
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser    
python manage.py runserver   
```

---

## GraphQL Endpoint

```
http://localhost:8000/graphql/
```

Strawberry provides a GraphiQL-like interface automatically.

---

# Queries

## 1. List all characters

```graphql
query {
  characters {
    name
  }
}
```

---

## 2. Filter characters by name

```graphql
query {
  characters(name: "luke") {
    name
  }
}
```

---

## 3. Get characters with films and planets

```graphql
query {
  characters {
    name
    films {
      title
      director
      openingCrawl
      planets {
        name
      }
    }
  }
}
```
---
# Mutations

## 1. Create a Planet

```graphql
mutation {
  createPlanet(name: "Tatooine") {
       id
      name
  }
}
```

---

## 2. Create a Film

```graphql
mutation {
  createFilm(
    title: "A New Hope"
    openingCrawl: "It is a period of civil war..."
    director: "George Lucas"
    producers: "Gary Kurtz"
    planetIds: [1]
  ) {
      id
      title
      director
      planets {
        name
      }
  }
}
```

---

## 3. Create a Character

```graphql
mutation {
  createCharacter(
    name: "Luke Skywalker"
    filmIds: [1]
  ) {
      id
      name
      films {
        title
      }
  }
}
```

## 4. Create another Planet (Hoth)
```graphql
mutation {
  createPlanet(name: "Hoth") {
      id
      name
  }
}
```

## 5. Create a Film with multiple planets (The Empire Strikes Back)
```graphql
mutation {
  createFilm(
    title: "The Empire Strikes Back"
    openingCrawl: "The battle against the Empire continues as rebel forces regroup..."
    director: "Irvin Kershner"
    producers: "Gary Kurtz"
    planetIds: [1, 2]   # e.g. Tatooine + Hoth depending on your DB
  ) {
      id
      title
      director
      planets {
        name
      }
  }
}
```

## 6. Create a Character with multiple films (Darth Vader)
```graphql
mutation {
  createCharacter(
    name: "Darth Vader"
    filmIds: [1, 2]
  ) {
      id
      name
      films {
        title
        director
      }
  }
}
```

---

# Running Tests

```bash
python manage.py test starwars.tests
```

---

# Future Improvements
* Pagination for large datasets
* Authentication (JWT)
* Integration with external API (SWAPI)
* Caching with Redis