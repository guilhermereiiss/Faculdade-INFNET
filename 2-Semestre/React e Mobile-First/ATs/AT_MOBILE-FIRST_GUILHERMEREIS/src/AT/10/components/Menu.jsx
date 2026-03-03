import { useState } from 'react';
import './MenuC.css';
import MinhaLogo from "../MINHALOGO.jpeg"


const Menu = () => {
  const [menuAberto, setMenuAberto] = useState(false);

  const alternarMenu = () => {
    setMenuAberto(!menuAberto);
  };

  return (
    <nav className={`menu ${menuAberto ? 'aberto' : ''}`}>
      <div className="menu_topo">
        <img src={MinhaLogo} alt="Logo" className="menu_logo" />
        <h1>Brand</h1>
        <button className="menu_botao" onClick={alternarMenu}>
          &#9776;
        </button>
      </div>
      <ul className={`menu_lista ${menuAberto ? 'visivel' : ''}`}>
        <li className="menu_item">Opção 1</li>
        <li className="menu_item">Opção 2</li>
        <li className="menu_item">Opção 3</li>
        <li className="menu_item">Opção 4</li>
      </ul>
    </nav>
  );
};

export default Menu;