import header from "./header.module.css";
import { VscMenu } from "react-icons/vsc";
import { useState } from "react";
import { Link } from "react-router-dom";
import { BsHighlights } from "react-icons/bs";

export default function Header() {
    const [menuAberto, setMenuAberto] = useState(false);

    const alternarMenu = () => {
        setMenuAberto(!menuAberto);
    };

    return (
        <header className={header.container_geral}>

            <Link to="/MatchMovie/home" clasName="cssanimation leFadeInLeft sequence">
                <h1 >
                    <span className={header.amarelo}>M</span>ovie<span className={header.laranja}>M</span>atch
                </h1>
            </Link>
            <div className={header.mini_header}>
                <button onClick={alternarMenu} className={header.menu_btn}>
                    <VscMenu />
                </button>

                <nav className={`${header.sidebar} ${menuAberto ? header.sidebar_ativo : ""}`}>
                    <ul className={header.menu_lista}>
                        <li >
                            <Link to="/MatchMovie/home">Home</Link>
                        </li>
                        <li>
                            <Link to="/MatchMovie/favoritos">Favoritos/Recomendações</Link>
                        </li>
                    </ul>
                </nav>
                <button onClick={() => {
          const tema = document.documentElement.getAttribute('data-tema')
          const proximoTema = tema === "escuro"? "claro" : "escuro";
          document.documentElement.setAttribute('data-tema', proximoTema);
          localStorage.setItem("@tema", proximoTema)
        }}>
          <BsHighlights />
        </button>
            </div>
        </header>
    );
}

