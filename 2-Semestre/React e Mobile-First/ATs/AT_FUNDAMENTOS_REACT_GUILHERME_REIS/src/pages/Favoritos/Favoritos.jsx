import Header from "../../Components/Header/header.jsx";
import FavoritosCSS from "./favoritos.module.css";
import 'react-toastify/dist/ReactToastify.css';
import { Link } from 'react-router-dom';
import { useState, useEffect } from "react";

export default function Favoritos() {
    const [favoritos, setFavoritos] = useState([]);

    useEffect(() => {
        const favoritosCarregados = localStorage.getItem("@favoritos");
        if (favoritosCarregados) {
            const favoritosConvertidos = JSON.parse(favoritosCarregados);
            setFavoritos(favoritosConvertidos);
        }
    }, []);

    return (
        <div className={FavoritosCSS.container_favoritos}>
            <Header />
            <h2>SEUS HOTEIS FAVORITOS ABAIXO</h2>
            <div className={FavoritosCSS.container_cards}>
                {favoritos.length === 0 ? (
                    <p>Nenhum hotel favoritado.</p>
                ) : (
                    favoritos.map(hotel => (
                        <div key={hotel.id} className={FavoritosCSS.card}>
                            
                                <Link to={`/AT_FUNDAMENTOS_REACT_GUILHERME_REIS/detalhes/${hotel.id}`}>


                                    <img src={hotel.imagem} alt={hotel.nome} className={FavoritosCSS.cardImagem} />
                                    <div className={FavoritosCSS.cardDetalhes}>
                                        <h3>{hotel.nome}</h3>
                                        <p>Preço: R${hotel.preco}</p>
                                        <p>Cidade: {hotel.cidade} - {hotel.estado}</p>
                                    </div>


                                </Link>
                            </div>
                        
                    ))
                )
                }
            </div >
        </div >
    );
}
