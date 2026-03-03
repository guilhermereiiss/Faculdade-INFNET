import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import './Detalhes.css';
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";

export default function Detalhes() {
    const { id } = useParams();
    const [detalhes, setDetalhes] = useState(null);
    const [trailer, setTrailer] = useState(null);
    const apiKey = "12374ecb147586c8d10ec01440db879d";

    const getDetalhes = async () => {
        try {
            const response = await axios.get(`https://api.themoviedb.org/3/movie/${id}`, {
                params: {
                    language: "pt-BR",
                    api_key: apiKey,
                },
            });
            setDetalhes(response.data);
            const videoResponse = await axios.get(`https://api.themoviedb.org/3/movie/${id}/videos`, {
                params: {
                    api_key: apiKey,
                    language: "pt-BR",
                },
            });
            const trailerKey = videoResponse.data.results.find(video => video.type === "Trailer")?.key;
            setTrailer(trailerKey);
        } catch (error) {
            console.error("Erro ao buscar detalhes:", error);
        }
    };

    useEffect(() => {
        getDetalhes();
    }, [id]);

    if (!detalhes) {
        return <div>Carregando...</div>;
    }

    return (
        <div>
            <Header />
            <div className="detalhes-container">
                <h1 className="detalhes-title">{detalhes.title}</h1>
                <p className="detalhes-rating">Nota: {detalhes.vote_average}</p>
                <p className="detalhes-release-date">Data de Lançamento: {new Date(detalhes.release_date).toLocaleDateString()}</p>
                <p className="detalhes-genres">Gêneros: {detalhes.genres.map(genre => genre.name).join(', ')}</p>
                <p className="detalhes-description">Descrição: {detalhes.overview}</p>

                {trailer && (
                    <div className="trailer-container">
                        <h2 className="trailer-title">Trailer</h2>
                        <iframe
                            className="trailer-iframe"
                            src={`https://www.youtube.com/embed/${trailer}`}
                            title="Trailer"
                            frameBorder="0"
                            allowFullScreen
                        ></iframe>
                    </div>
                )}
            </div>
            <Footer/>
        </div>
    );
}
