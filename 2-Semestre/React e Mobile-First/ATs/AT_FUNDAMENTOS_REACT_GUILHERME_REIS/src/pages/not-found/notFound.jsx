import notFound from "./notFound.module.css"
import { Link } from "react-router-dom"; 

export default function NotFound() {
    return (
        <div className={notFound.container}>
            <h1 className={notFound.titulo}>404: Página Não Encontrada</h1>
            <p className={notFound.descricao}>A página que você está procurando não existe.</p>

            <Link to="/AT_FUNDAMENTOS_REACT_GUILHERME_REIS/" className={notFound.botao_voltar}> 
                Voltar para Home
            </Link>
        </div>
    )
}

