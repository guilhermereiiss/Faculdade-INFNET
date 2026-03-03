import header from "./header.module.css";
import { VscColorMode, VscMenu } from "react-icons/vsc"; 
import { useState } from "react"; 
import { Link } from "react-router-dom";

export default function Header() {
  const [menuAberto, setMenuAberto] = useState(false); 

  const alternarMenu = () => {
    setMenuAberto(!menuAberto); 
  };

  return (
    <header className={header.container_geral}>
      <h1 className="cssanimation lePeek sequence">
        <span className={header.amarelo}>G</span>ui<span className={header.laranja}>V</span>ago
      </h1>

      <div className={header.mini_header}>
        <button onClick={alternarMenu} className={header.menu_btn}>
          <VscMenu />
        </button>

        <nav className={`${header.sidebar} ${menuAberto ? header.sidebar_ativo : ""}`}>
          <ul className={header.menu_lista}>
            <li >
              <Link to="/AT_FUNDAMENTOS_REACT_GUILHERME_REIS/">Home</Link>
            </li>
            <li>
              <Link to="/AT_FUNDAMENTOS_REACT_GUILHERME_REIS/favoritos">Favoritos</Link>
            </li>
          </ul>
        </nav>

        <button onClick={() => {
          const tema = document.documentElement.getAttribute('data-tema')
          const proximoTema = tema === "escuro"? "claro" : "escuro";
          document.documentElement.setAttribute('data-tema', proximoTema);
          localStorage.setItem("@tema", proximoTema)
        }}>
          <VscColorMode />
        </button>

      </div>
    </header>
  );
}

