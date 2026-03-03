
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { obterFavoritos, removerFavorito } from "../../components/Favoritar/FavoritarFunc";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";
import "./Favoritos.css";

export default function Favoritos() {
    const [favoritos, setFavoritos] = useState([]);
    const [itensFavoritos, setItensFavoritos] = useState([]);
    const [recomendados, setRecomendados] = useState([]);  
    const apiKey = "12374ecb147586c8d10ec01440db879d";

    useEffect(() => {
        const idsFavoritos = obterFavoritos();
        setFavoritos(idsFavoritos);
        buscarFavoritos(idsFavoritos);
    }, []);

    const buscarFavoritos = async (ids) => {
        try {
            const requisicoes = ids.map((id) =>
                axios.get(`https://api.themoviedb.org/3/movie/${id}`, {
                    params: { api_key: apiKey, language: "pt-BR" },
                }).catch(() =>
                    axios.get(`https://api.themoviedb.org/3/tv/${id}`, {
                        params: { api_key: apiKey, language: "pt-BR" },
                    })
                )
            );

            const respostas = await Promise.all(requisicoes);
            const resultados = respostas.map((res) => res.data);
            setItensFavoritos(resultados);

         
            const generos = resultados.flatMap(item => item.genres.map(genre => genre.id));
            buscarRecomendados(generos);
        } catch (error) {
            console.error("Erro ao buscar favoritos:", error);
        }
    };

    const buscarRecomendados = async (generos) => {
        try {
            
            const requisicoes = generos.map((genero) =>
                axios.get(`https://api.themoviedb.org/3/discover/movie`, {
                    params: { 
                        api_key: apiKey, 
                        language: "pt-BR", 
                        with_genres: genero,
                        page: 1 
                    }
                })
            );

            const respostas = await Promise.all(requisicoes);
            const filmesRecomendados = respostas.flatMap((res) => res.data.results);
            setRecomendados(filmesRecomendados);
        } catch (error) {
            console.error("Erro ao buscar filmes recomendados:", error);
        }
    };

    const handleRemoverFavorito = (id) => {
        removerFavorito(id);
        setFavoritos((prev) => prev.filter((fav) => fav !== id));
        setItensFavoritos((prev) => prev.filter((item) => item.id !== id));
    };

    const renderizarItem = (item) => (
        <div key={item.id} className="favorito-item">
            <Link to={`/MatchMovie/detalhes/${item.id}`}>
                <div className="movie-card">
                    <img
                        src={
                            item.poster_path
                                ? `https://image.tmdb.org/t/p/w500${item.poster_path}`
                                : "https://via.placeholder.com/500x750?text=Imagem+Indisponível"
                        }
                        alt={item.title || item.name}
                        className="movie-poster"
                    />
                    <div className="movie-info">
                        <h2>{item.title || item.name}</h2>
                        <p>Nota: {item.vote_average}</p>
                        <p>
                            Data de lançamento:{" "}
                            {new Date(item.release_date || item.first_air_date).toLocaleDateString()}
                        </p>
                        <button onClick={(e) => {
                            e.preventDefault();
                            e.stopPropagation();
                            handleRemoverFavorito(item.id);
                        }}>
                            Remover Favorito
                        </button>
                    </div>
                </div>
            </Link>
        </div>
    );

    const renderizarRecomendado = (item) => (
        <div key={item.id} className="recomendado-item">
            <Link to={`/MatchMovie/detalhes/${item.id}`}>
                <div className="movie-card">
                    <img
                        src={
                            item.poster_path
                                ? `https://image.tmdb.org/t/p/w500${item.poster_path}`
                                : "https://via.placeholder.com/500x750?text=Imagem+Indisponível"
                        }
                        alt={item.title || item.name}
                        className="movie-poster"
                    />
                    <div className="movie-info">
                        <h2>{item.title || item.name}</h2>
                        <p>Nota: {item.vote_average}</p>
                        <p>
                            Data de lançamento:{" "}
                            {new Date(item.release_date || item.first_air_date).toLocaleDateString()}
                        </p>
                    </div>
                </div>
            </Link>
        </div>
    );

    return (
        <div className="container-fav">
            <Header />
            <div className="favoritos-titulo">
                <h1>Meus Favoritos</h1>
            </div>
            <div className="favoritos-container">
                {itensFavoritos.length > 0 ? (
                    itensFavoritos.map((item) => renderizarItem(item))
                ) : (
                    <p>Nenhum favorito encontrado.</p>
                )}
            </div>

            <div className="favoritos-titulo">
                <h1>Filmes Recomendados</h1>
            </div>
            <div className="favoritos-container">
                {recomendados.length > 0 ? (
                    recomendados.map((item) => renderizarRecomendado(item))
                ) : (
                    <p>Sem recomendações disponíveis no momento.</p>
                )}
            </div>

            <Footer />
        </div>
    );
}
