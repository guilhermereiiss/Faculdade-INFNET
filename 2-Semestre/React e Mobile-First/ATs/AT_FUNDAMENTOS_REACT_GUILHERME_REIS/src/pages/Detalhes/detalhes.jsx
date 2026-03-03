import Header from "../../Components/Header/header.jsx"
import detalhes from './detalhes.module.css'
import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';

export default function Detalhes() {

    const { id } = useParams();
    const [hotel, setHotel] = useState(null);

    useEffect(() => {
        const hoteis = JSON.parse(localStorage.getItem('@hoteis')) || [];
        const hotelSelecionado = hoteis.find(hotel => hotel.id === id);
        setHotel(hotelSelecionado);
    }, [id]);

    if (!hotel) {
        return <p>Hotel não encontrado.</p>;
    }
    return (
        <div >
            <Header />

            <div className={detalhes.container_detalhes}>
                <div className={detalhes.container_detalhes_sla}>
                    <img src={hotel.imagem} alt={hotel.nome} />
                    <div className={detalhes.Conteudo}>
                        <h2>{hotel.nome}</h2>
                        <p><span>Preço:</span> R${hotel.preco}</p>
                        <p><span>Cidade:</span> {hotel.cidade} - {hotel.estado}</p>
                        <p><span>Nota:</span> {hotel.classificacao}</p>
                        <p><span>Descrição:</span> {hotel.descricao}</p>
                        <p><span>FeedBack:</span> {hotel.feedback}</p>
                    </div>
                </div>

                <div className={detalhes.organizaImgAdd}>
                    <img src={hotel.imagemAdd1} alt={hotel.nome} />
                    <img src={hotel.imagemAdd2} alt={hotel.nome} />
                    <img src={hotel.imagemAdd3} alt={hotel.nome} />
                    <img src={hotel.imagemAdd4} alt={hotel.nome} />
                </div>
            </div>
        </div>
    )
}