import  { useState } from 'react';
import './Menu.css';
import MinhaLogo from "./MINHALOGO.jpeg"

const Menu = () => {
  const [menuAberto, setMenuAberto] = useState(false);

  const alternarMenu = () => {
    setMenuAberto(!menuAberto);
  };

  return (
    <nav className={`menu ${menuAberto ? 'aberto' : ''}`}>
      <div className="menu_topo">
        <img src={MinhaLogo} alt="Logo" className="menu_logo" />
        <button className="menu_botao" onClick={alternarMenu}>
          &#9776;
        </button>
      </div>
      <ul className={`menu_lista ${menuAberto ? 'visivel' : ''}`}>
        <li className="menu_item">Perfil</li>
        <li className="menu_item">Postagens</li>
        <li className="menu_item">Amigos</li>
        <li className="menu_item">Fotos</li>
        <li className="menu_item">Vídeos</li>
        <li className="menu_item">Configurações</li>
      </ul>
    </nav>
  );
};

export default Menu;
