"use client";

import { useQuery } from "@apollo/client/react";
import { useRouter } from "next/navigation";
import { GET_CHARACTERS } from "@/graphql/queries/characters";
import { GetCharactersResponse } from "@/graphql/types/character";

export default function Home() {
  const router = useRouter();
  const { data, loading, error } =
    useQuery<GetCharactersResponse>(GET_CHARACTERS);

  if (loading) return <p className="p-6">Loading...</p>;
  if (error) return <p className="p-6">Error: {error.message}</p>;

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold text-center mb-8">
        Star Wars Explorer 
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {data?.characters.map((char) => (
          <div
            key={char.id}
            className="bg-white p-5 rounded-xl shadow hover:shadow-lg transition"
          >
            <h2 className="text-lg font-semibold">{char.name}</h2>

            <button
              onClick={() => router.push(`/character/${char.id}`)}
              className="mt-4 w-full bg-blue-500 hover:bg-blue-600 transition text-white py-2 rounded-lg font-medium"
            >
              View Details
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}