import { useState } from 'react';
import './MenuC.css';
import MinhaLogo from "../MINHALOGO.jpeg"

export default function Menu() {
  const [menuExpandido, setMenuExpandido] = useState(false);

  const alternarMenu = () => {
    setMenuExpandido(!menuExpandido);
  };

  return (
    <div className="menu">
      <div className='menu-header'>
        <button className="botao-menu" onClick={alternarMenu}>
        ☰
        </button>
        <h1>Brand</h1>
        <img src={MinhaLogo} alt="Logo" className="menu_logo" />
      </div>

      <div className='menu-funcional'>
      <ul className={`menu-items ${menuExpandido ? 'expandido' : ''}`}>
        <li className="menu-item">Opção 1</li>
        <li className="menu-item">Opção 2</li>
        <li className="menu-item">Opção 3</li>
        <li className="menu-item">Opção 4</li>
      </ul>
      </div>
    </div>
  );
}
