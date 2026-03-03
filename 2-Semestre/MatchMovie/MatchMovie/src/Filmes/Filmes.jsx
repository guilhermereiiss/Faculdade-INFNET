
import { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import { adicionarFavorito, removerFavorito, obterFavoritos } from '../components/Favoritar/FavoritarFunc';
import './FilmesGerais.css';

export default function FilmesGerais() {
    const [movies, setMovies] = useState([]);
    const [series, setSeries] = useState([]);
    const [favoritos, setFavoritos] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');
    const [isSearchActive, setIsSearchActive] = useState(false);  
    const apiKey = "12374ecb147586c8d10ec01440db879d";

    const getFilmesESeries = async (search = '') => {
        try {
            const [filmesResponse, seriesResponse] = await Promise.all([
                axios.get("https://api.themoviedb.org/3/discover/movie", {
                    params: {
                        language: "pt-BR",
                        api_key: apiKey,
                    },
                }),
                axios.get("https://api.themoviedb.org/3/discover/tv", {
                    params: {
                        language: "pt-BR",
                        api_key: apiKey,
                    },
                }),
            ]);

            setMovies(filmesResponse.data.results);
            setSeries(seriesResponse.data.results);
        } catch (error) {
            console.error("Erro ao buscar filmes e séries:", error);
        }
    };

    const buscar = async () => {
        if (!searchTerm.trim()) {
            getFilmesESeries();
            return;
        }

        try {
            const [filmesResponse, seriesResponse] = await Promise.all([
                axios.get("https://api.themoviedb.org/3/search/movie", {
                    params: {
                        query: searchTerm,
                        language: "pt-BR",
                        api_key: apiKey,
                    },
                }),
                axios.get("https://api.themoviedb.org/3/search/tv", {
                    params: {
                        query: searchTerm,
                        language: "pt-BR",
                        api_key: apiKey,
                    },
                }),
            ]);

            setMovies(filmesResponse.data.results);
            setSeries(seriesResponse.data.results);
        } catch (error) {
            console.error("Erro ao buscar filmes e séries:", error);
        }
    };

    useEffect(() => {
        getFilmesESeries();
        setFavoritos(obterFavoritos());
    }, []);

    useEffect(() => {
        buscar();
    }, [searchTerm]);

    const handleFavoritar = (id) => {
        if (favoritos.includes(id)) {
            removerFavorito(id);
            setFavoritos(prev => prev.filter(favorito => favorito !== id));
        } else {
            adicionarFavorito(id);
            setFavoritos(prev => [...prev, id]);
        }
    };

    const renderMovieCard = (movie, type) => (
        <div key={`${type}-${movie.id}`}>
            <Link to={`/MatchMovie/detalhes/${movie.id}`}>
                <div className="movie-card">
                    <img
                        src={
                            movie.poster_path
                                ? `https://image.tmdb.org/t/p/w500${movie.poster_path}`
                                : "https://via.placeholder.com/500x750?text=Imagem+Indisponível"
                        }
                        alt={type === 'movie' ? movie.title : movie.name}
                        className="movie-poster"
                    />
                    <div className="movie-info">
                        <h2>{type === 'movie' ? movie.title : movie.name}</h2>
                        <p>Nota: {movie.vote_average}</p>
                        <p>Data de lançamento: {new Date(type === 'movie' ? movie.release_date : movie.first_air_date).toLocaleDateString()}</p>
                        <button onClick={(e) => {
                            e.preventDefault();
                            e.stopPropagation();
                            handleFavoritar(movie.id);
                        }}>
                            {favoritos.includes(movie.id) ? 'Remover Favorito' : 'Favoritar'}
                        </button>
                    </div>
                </div>
            </Link>
        </div>
    );

    return (
        <div className="geral">
            <div className="search-container">
                <div
                    className={`search-input-container ${isSearchActive ? 'active' : ''}`}
                    onClick={() => setIsSearchActive(true)}  
                >
                    <i className="fa fa-search" style={{ fontSize: '20px', color: '#aaa' }}></i>  {/* Ícone de busca */}
                    <input
                        type="text"
                        placeholder="Buscar filmes ou séries..."
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                        className="search-input"
                    />
                </div>
            </div>
            <div className="movie-container">
                {movies.map((movie) => renderMovieCard(movie, 'movie'))}
                {series.map((serie) => renderMovieCard(serie, 'tv'))}
            </div>
        </div>
    );
}
