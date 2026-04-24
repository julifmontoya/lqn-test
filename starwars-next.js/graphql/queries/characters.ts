import { gql } from "@apollo/client";

export const GET_CHARACTERS = gql`
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
`;