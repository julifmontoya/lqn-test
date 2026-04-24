"use client";

import { useQuery } from "@apollo/client/react";
import { useParams, useRouter } from "next/navigation";
import { GET_CHARACTERS } from "@/graphql/queries/characters";
import { GetCharactersResponse } from "@/graphql/types/character";

export default function CharacterModal() {
  const { id } = useParams();
  const router = useRouter();
  const { data, loading } =
    useQuery<GetCharactersResponse>(GET_CHARACTERS);
  if (loading) return null;
  const character = data?.characters.find((c) => c.id === id);
  if (!character) return <p>Not found</p>;

  return (
    <div
      className="fixed inset-0 bg-black/60 flex items-center justify-center"
      onClick={() => router.push("/")}
    >
      <div
        className="bg-white p-6 rounded-xl w-full max-w-lg shadow-xl"
        onClick={(e) => e.stopPropagation()}
      >
        <h2 className="text-xl font-bold">{character.name}</h2>
        <div className="mt-4">
          <h3 className="font-semibold mb-2">Films</h3>
          {character.films.map((film) => (
            <div key={film.title} className="mb-4">
              <p className="font-medium">{film.title}</p>
              <p className="text-sm text-gray-600">
                Director: {film.director}
              </p>

              <div className="flex flex-wrap gap-2 mt-2">
                {film.planets.map((p, index) => (
                  <span
                    key={`${p.id}-${index}`}
                    className="bg-gray-200 px-2 py-1 rounded text-xs"
                  >
                    {p.name}
                  </span>
                ))}
              </div>
            </div>
          ))}
        </div>
        <button
          onClick={() => router.push("/")}
          className="mt-4 w-full bg-blue-500 hover:bg-blue-600 text-white px-3 py-2 rounded-lg"
        >
          Close
        </button>
      </div>
    </div>
  );
}