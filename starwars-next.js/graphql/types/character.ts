export type Planet = {
  id: string;
  name: string;
};

export type Film = {
  title: string;
  director: string;
  planets: Planet[];
};

export type Character = {
  id: string;
  name: string;
  films: Film[];
};

export type GetCharactersResponse = {
  characters: Character[];
};