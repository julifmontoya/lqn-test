# Star Wars Explorer (Next.js + Django GraphQL)

## 🚀 Overview

Star Wars Explorer is a modern web application built with **Next.js (App Router + TypeScript)** and powered by a **Django + Strawberry GraphQL API**.

The app allows users to:

* Browse Star Wars characters
* View detailed information in a modal
* Explore films, directors, and planets
* Navigate directly via URL (deep linking)

---

## 🧠 Architecture

The project follows a **clean, scalable architecture**:

```
starwars-frontend/
├── app/                 # Next.js App Router pages
│   ├── page.tsx         # Characters list
│   ├── character/[id]   # Character modal route
│   ├── layout.tsx       # Root layout
│   ├── providers.tsx    # Apollo Provider
│
├── graphql/             # GraphQL layer
│   ├── queries/         # Queries
│   ├── types/           # TypeScript types
│
├── lib/                 # Infrastructure
│   └── apollo.ts        # Apollo Client setup
│
├── .env                 
```

---

## Tech Stack
### Frontend
* Next.js (App Router)
* React + TypeScript
* Tailwind CSS v4
* Apollo Client (GraphQL)

### Backend
* Django
* Strawberry GraphQL

---

## GraphQL Integration
The app consumes a GraphQL API using Apollo Client.

Example query:

```graphql
query {
  characters {
    id
    name
    films {
      title
      director
      planets {
        id
        name
      }
    }
  }
}
```

---

## Environment Variables

Create a `.env.local` file:

```env
NEXT_PUBLIC_GRAPHQL_URL=http://localhost:8000/graphql/
```

---

## Getting Started

### 1. Clone the repo

```bash
git clone <your-repo>
cd starwars-frontend
```

---

### 2. Install dependencies

```bash
npm install
```

---

### 3. Run the development server

```bash
npm run dev
```

Open:

```
http://localhost:3000
```

---

## Features

* Character listing with responsive grid
* Modal with films, directors, and planets
* URL-based routing (`/character/[id]`)
* Deep linking (refresh keeps modal open)
* Modern UI with Tailwind CSS
* Fast GraphQL data fetching with Apollo

---