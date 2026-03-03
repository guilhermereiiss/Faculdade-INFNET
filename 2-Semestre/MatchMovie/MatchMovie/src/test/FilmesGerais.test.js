import { render, screen, fireEvent, waitFor } from "@testing-library/react";

import FilmesGerais from "../Filmes/Filmes";
import axios from "axios";
import { adicionarFavorito, removerFavorito, obterFavoritos } from "../components/Favoritar/FavoritarFunc";

jest.mock("axios");
jest.mock("../components/Favoritar/FavoritarFunc", () => ({
  adicionarFavorito: jest.fn(),
  removerFavorito: jest.fn(),
  obterFavoritos: jest.fn().mockReturnValue([]),
}));

describe("FilmesGerais Component", () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  test("renders search input", () => {
    render(<FilmesGerais />);
    const searchInput = screen.getByPlaceholderText("Buscar filmes ou séries...");
    expect(searchInput).toBeInTheDocument();
  });

  test("fetches and displays movies and series on load", async () => {
    axios.get.mockResolvedValueOnce({
      data: { results: [{ id: 1, title: "Movie 1", poster_path: null, vote_average: 8, release_date: "2024-12-01" }] },
    });
    axios.get.mockResolvedValueOnce({
      data: { results: [{ id: 2, name: "Series 1", poster_path: null, vote_average: 9, first_air_date: "2024-11-01" }] },
    });

    render(<FilmesGerais />);

    await waitFor(() => expect(screen.getByText("Movie 1")).toBeInTheDocument());
    expect(screen.getByText("Series 1")).toBeInTheDocument();
  });

  test("handles search input and fetches results", async () => {
    axios.get.mockResolvedValueOnce({
      data: { results: [{ id: 3, title: "Searched Movie", poster_path: null, vote_average: 7, release_date: "2024-10-01" }] },
    });
    axios.get.mockResolvedValueOnce({
      data: { results: [] },
    });

    render(<FilmesGerais />);

    const searchInput = screen.getByPlaceholderText("Buscar filmes ou séries...");
    fireEvent.change(searchInput, { target: { value: "Searched" } });

    await waitFor(() => expect(screen.getByText("Searched Movie")).toBeInTheDocument());
  });

  test("favorites a movie and updates the UI", async () => {
    const mockMovie = { id: 1, title: "Movie 1", poster_path: null, vote_average: 8, release_date: "2024-12-01" };

    axios.get.mockResolvedValueOnce({
      data: { results: [mockMovie] },
    });
    axios.get.mockResolvedValueOnce({ data: { results: [] } });
    obterFavoritos.mockReturnValue([]);

    render(<FilmesGerais />);

    await waitFor(() => expect(screen.getByText("Movie 1")).toBeInTheDocument());

    const favoriteButton = screen.getByText("Favoritar");
    fireEvent.click(favoriteButton);

    expect(adicionarFavorito).toHaveBeenCalledWith(mockMovie.id);
    expect(screen.getByText("Remover Favorito")).toBeInTheDocument();
  });

  test("removes a movie from favorites and updates the UI", async () => {
    const mockMovie = { id: 1, title: "Movie 1", poster_path: null, vote_average: 8, release_date: "2024-12-01" };

    axios.get.mockResolvedValueOnce({
      data: { results: [mockMovie] },
    });
    axios.get.mockResolvedValueOnce({ data: { results: [] } });
    obterFavoritos.mockReturnValue([mockMovie.id]);

    render(<FilmesGerais />);

    await waitFor(() => expect(screen.getByText("Movie 1")).toBeInTheDocument());

    const unfavoriteButton = screen.getByText("Remover Favorito");
    fireEvent.click(unfavoriteButton);

    expect(removerFavorito).toHaveBeenCalledWith(mockMovie.id);
    expect(screen.getByText("Favoritar")).toBeInTheDocument();
  });
});
