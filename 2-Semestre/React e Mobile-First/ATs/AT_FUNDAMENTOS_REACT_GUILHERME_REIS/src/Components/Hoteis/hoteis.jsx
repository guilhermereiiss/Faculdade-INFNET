import { useState, useEffect } from 'react';
import Modal from 'react-modal';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { Link } from 'react-router-dom';
import { nanoid } from 'nanoid';
import { SiHotelsdotcom } from "react-icons/si";
import Hotel from './hoteis.module.css';
import { ToastSucesso, ToastErro } from "./toast.jsx";

const customStyles = {
    content: {
        top: '50%',
        left: '50%',
        right: 'auto',
        bottom: 'auto',
        marginRight: '-50%',
        transform: 'translate(-50%, -50%)',
    },
};

export default function Hoteis() {
    const [modalIsOpen, setIsOpen] = useState(false);
    const [formulario, setFormulario] = useState({
        imagem: '',
        classificacao: '',
        cidade: '',
        nome: '',
        estado: '',
        preco: '',
        descricao: '',
        feedback: '',
        imagemAdd1: '',
        imagemAdd2: '',
        imagemAdd3: '',
        imagemAdd4: '',
    });

    const [pesquisa, setPesquisa] = useState('');
    const [hoteis, setHoteis] = useState([]);
    const [favoritos, setFavoritos] = useState([]);
    const [hotelEditando, setHotelEditando] = useState(null);
    const [ordenacao, setOrdenacao] = useState('preco');

    function openModal() {
        setIsOpen(true);
        setHotelEditando(null);
        setFormulario({
            imagem: '',
            classificacao: '',
            cidade: '',
            nome: '',
            estado: '',
            preco: '',
            descricao: '',
            feedback: '',
            imagemAdd1: '',
            imagemAdd2: '',
            imagemAdd3: '',
            imagemAdd4: '',
        });
    }

    function closeModal() {
        setIsOpen(false);
    }

    function carregarHoteisBD() {
        const hoteisCarregados = localStorage.getItem("@hoteis");
        if (hoteisCarregados) {
            const hoteisConvertidos = JSON.parse(hoteisCarregados);
            setHoteis(hoteisConvertidos);
        }
    }

    function carregarFavoritosBD() {
        const favoritosCarregados = localStorage.getItem("@favoritos");
        if (favoritosCarregados) {
            const favoritosConvertidos = JSON.parse(favoritosCarregados);
            setFavoritos(favoritosConvertidos);
        }
    }

    useEffect(() => {
        carregarHoteisBD();
        carregarFavoritosBD();
    }, []);


    const salvarHotel = (event) => {
        event.preventDefault();

        if (!formulario.imagem || !formulario.nome || !formulario.cidade ||
            !formulario.estado || !formulario.preco || formulario.preco <= 0 ||
            !formulario.descricao || !formulario.feedback) {

            toast.error("Preencha todos os campos obrigatórios antes de salvar", {
                style: ToastErro,
                hideProgressBar: true
            });
            return;
        }

        if (hotelEditando) {
            const hoteisAtualizados = hoteis.map(hotel =>
                hotel.id === hotelEditando.id ? { ...formulario, id: hotelEditando.id } : hotel
            );
            setHoteis(hoteisAtualizados);
            localStorage.setItem('@hoteis', JSON.stringify(hoteisAtualizados));
            toast.success("Hotel editado com sucesso!", {
                style: ToastSucesso,
                hideProgressBar: true
            });
            setHotelEditando(null);
        } else {
            const ID = nanoid();
            const novosHoteis = [...hoteis, { ...formulario, id: ID }];
            setHoteis(novosHoteis);

            localStorage.setItem('@hoteis', JSON.stringify(novosHoteis));
            toast.success("Hotel salvo com sucesso!", {
                style: ToastSucesso,
                hideProgressBar: true
            });
        }

        setIsOpen(false);
    };
    const removerHotel = (id) => {
        const hoteisFiltrados = hoteis.filter((hotel) => hotel.id !== id);
        setHoteis(hoteisFiltrados);
        localStorage.setItem("@hoteis", JSON.stringify(hoteisFiltrados));
    };

    const openModalEditar = (hotel) => {
        setFormulario(hotel);
        setHotelEditando(hotel);
        setIsOpen(true);
    };

    const adicionarFavorito = (hotel) => {
        const novosFavoritos = [...favoritos, hotel];
        setFavoritos(novosFavoritos);
        localStorage.setItem("@favoritos", JSON.stringify(novosFavoritos));
        toast.success("Hotel adicionado aos favoritos!", { hideProgressBar: true });
    };

    const removerFavorito = (id) => {
        const favoritosAtualizados = favoritos.filter((hotel) => hotel.id !== id);
        setFavoritos(favoritosAtualizados);
        localStorage.setItem("@favoritos", JSON.stringify(favoritosAtualizados));
        toast.success("Hotel removido dos favoritos!", { hideProgressBar: true });
    };

    const toggleFavorito = (hotel) => {
        if (favoritos.some(fav => fav.id === hotel.id)) {
            removerFavorito(hotel.id);
        } else {
            adicionarFavorito(hotel);
        }
    };


    const ordenarHoteis = (criterio) => {
        const hoteisOrdenados = [...hoteis].sort((a, b) => {
            if (criterio === 'preco') {
                return a.preco - b.preco;
            } else if (criterio === 'classificacao') {
                return b.classificacao - a.classificacao;
            }
            return 0;
        });
        return hoteisOrdenados;
    };

    const hoteisOrdenados = ordenarHoteis(ordenacao);

    const CardHotel = ({ hotel }) => (
        <div className={Hotel.card}>
            <Link to={`/AT_FUNDAMENTOS_REACT_GUILHERME_REIS/detalhes/${hotel.id}`}>
                <img src={hotel.imagem} alt={hotel.nome} className={Hotel.cardImagem} />
                <div className={Hotel.cardDetalhes}>
                    <h3>{hotel.nome}</h3>
                    <p>Preço: R${hotel.preco}</p>
                    <p>Cidade: {hotel.cidade} - {hotel.estado}</p>
                    <p>Nota: {hotel.classificacao}</p>
                </div>
            </Link>

            <div className={Hotel.organiza_btn}>
                <button onClick={() => removerHotel(hotel.id)} className={Hotel.btn_remover}>Remover</button>
                <button onClick={() => openModalEditar(hotel)} className={Hotel.btn_editar}>Editar</button>
                <button onClick={() => toggleFavorito(hotel)} className={Hotel.btn_favoritar}>
                    {favoritos.some(fav => fav.id === hotel.id) ? 'Desfavoritar' : 'Favoritar'}
                </button>
            </div>
        </div>
    );

    const HoteisFiltrados = hoteisOrdenados.filter(hotel =>
        (hotel.nome.toLowerCase().includes(pesquisa.toLowerCase())) ||
        (hotel.cidade.toLowerCase().includes(pesquisa.toLowerCase())) ||
        (hotel.estado.toLowerCase().includes(pesquisa.toLowerCase()))
    )

    return (
        <div>

            <div className={Hotel.organizaContainer}>
                <div className={Hotel.ordenacaoContainer}>
                    <label htmlFor="ordenacao" className={Hotel.ordenacaoLabel}>Ordenar por:</label>
                    <select
                        id="ordenacao"
                        value={ordenacao}
                        onChange={(e) => setOrdenacao(e.target.value)}
                        className={Hotel.ordenacaoSelect}
                    >
                        <option value="preco">Preço</option>
                        <option value="classificacao">Classificação</option>
                    </select>
                </div>

                <div className={Hotel.barraPesquisa}>
                    <input
                        type="search"
                        placeholder="Pesquise aqui 🔍"
                        value={pesquisa}
                        className={Hotel.ordenacaoSelect}
                        onChange={(e) => setPesquisa(e.target.value)}
                    />
                </div>
            </div>
            <button className={Hotel.Modal_Btn} onClick={openModal}><SiHotelsdotcom /></button>
            <Modal
                isOpen={modalIsOpen}
                onRequestClose={closeModal}
                style={customStyles}
                contentLabel="Cadastro de Hotel"
            >
                <div className={Hotel.formularioContainer}>
                    <form onSubmit={salvarHotel}>
                        <div className={Hotel.imagem_form}>
                            <label htmlFor="imagem">Imagem:</label>
                            <input
                                placeholder='Importe uma imagem'
                                type="text"
                                name="imagem"
                                value={formulario.imagem}
                                onChange={(event) =>
                                    setFormulario({ ...formulario, imagem: event.target.value })}
                            />
                        </div>

                        <div className={Hotel.imagem_form}>
                            <label htmlFor="imagem">Imagem Adicional 1:</label>
                            <input
                                placeholder='Importe uma imagem'
                                type="text"
                                name="imagem"
                                value={formulario.imagemAdd1}
                                onChange={(event) =>
                                    setFormulario({ ...formulario, imagemAdd1: event.target.value })}
                            />
                        </div>

                        <div className={Hotel.imagem_form}>
                            <label htmlFor="imagem">Imagem Adicional 2:</label>
                            <input
                                placeholder='Importe uma imagem'
                                type="text"
                                name="imagem"
                                value={formulario.imagemAdd2}
                                onChange={(event) =>
                                    setFormulario({ ...formulario, imagemAdd2: event.target.value })}
                            />
                        </div>

                        <div className={Hotel.imagem_form}>
                            <label htmlFor="imagem">Imagem Adicional 3:</label>
                            <input
                                placeholder='Importe uma imagem'
                                type="text"
                                name="imagem"
                                value={formulario.imagemAdd3}
                                onChange={(event) =>
                                    setFormulario({ ...formulario, imagemAdd3: event.target.value })}
                            />
                        </div>

                        <div className={Hotel.imagem_form}>
                            <label htmlFor="imagem">Imagem Adicional 4:</label>
                            <input
                                placeholder='Importe uma imagem'
                                type="text"
                                name="imagem"
                                value={formulario.imagemAdd4}
                                onChange={(event) =>
                                    setFormulario({ ...formulario, imagemAdd4: event.target.value })}
                            />
                        </div>

                        <div>
                            <label htmlFor="nome">Nome do Hotel:</label>
                            <input
                                type="text"
                                name="nome"
                                value={formulario.nome}
                                onChange={(event) =>
                                    setFormulario({ ...formulario, nome: event.target.value })}
                            />
                        </div>

                        <div>
                            <label htmlFor="classificacao">Nota (1-5):</label>
                            <input
                                type="text"
                                name="classificacao"
                                value={formulario.classificacao}
                                onChange={(event) =>
                                    setFormulario({ ...formulario, classificacao: event.target.value })}
                            />
                        </div>

                        <div>
                            <label htmlFor="cidade">Cidade:</label>
                            <input
                                type="text"
                                name="cidade"
                                value={formulario.cidade}
                                onChange={(event) =>
                                    setFormulario({ ...formulario, cidade: event.target.value })}
                            />
                        </div>

                        <div>
                            <label htmlFor="estado">Estado:</label>
                            <input
                                type="text"
                                name="estado"
                                value={formulario.estado}
                                onChange={(event) =>
                                    setFormulario({ ...formulario, estado: event.target.value })}
                            />
                        </div>

                        <div>
                            <label htmlFor="preco">Preço:</label>
                            <input
                                type="number"
                                name="preco"
                                value={formulario.preco}
                                onChange={(event) =>
                                    setFormulario({ ...formulario, preco: event.target.value })}
                            />
                        </div>

                        <div className={Hotel.Vertical_Form}>
                            <label htmlFor="descricao">Descrição:</label>
                            <textarea
                                name="descricao"
                                value={formulario.descricao}
                                onChange={(event) =>
                                    setFormulario({ ...formulario, descricao: event.target.value })}
                            />
                        </div>

                        <div className={Hotel.Vertical_Form}>
                            <label htmlFor="feedback">Feedback:</label>
                            <textarea
                                name="feedback"
                                value={formulario.feedback}
                                onChange={(event) =>
                                    setFormulario({ ...formulario, feedback: event.target.value })}
                            />
                        </div>

                        <div>
                            <button type="submit">{hotelEditando ? 'Editar' : 'Salvar'}</button>
                            <button onClick={closeModal}>Cancelar</button>
                        </div>
                    </form>
                </div>
            </Modal>

            <div className={Hotel.cardsContainer}>
                {HoteisFiltrados.length === 0 ? (
                    <p>Nenhum hotel cadastrado.</p>
                ) : (
                    HoteisFiltrados.map(hotel => (
                        <CardHotel key={hotel.id} hotel={hotel} />
                    ))
                )}
            </div>

            <ToastContainer />
        </div>
    );
}