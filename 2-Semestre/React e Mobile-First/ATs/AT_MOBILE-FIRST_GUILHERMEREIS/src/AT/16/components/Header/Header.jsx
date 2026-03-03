import MinhaLogo from "./MINHALOGO.jpeg";
import { useState } from "react";
import styles from "./HeaderC.module.css";

const Menu = () => {
  const [menuAberto, setMenuAberto] = useState(false);

  const alternarMenu = () => {
    setMenuAberto(!menuAberto);
  };

  return (
    <nav className={`${styles.menu} ${menuAberto ? styles.aberto : ""}`}>
      <div className={styles.menu_topo}>
        <img src={MinhaLogo} alt="Logo" className={styles.menu_logo} />
        <h1 className={styles.h1}>DESPEGA OLgui</h1>
        <button className={styles.menu_botao} onClick={alternarMenu}>
          &#9776;
        </button>
      </div>
      <ul className={`${styles.menu_lista} ${menuAberto ? styles.visivel : ""}`}>
        <li className={styles.menu_item}>Home</li>
        <li className={styles.menu_item}>Produtos</li>
        <li className={styles.menu_item}>Saiba Mais</li>
        <li className={styles.menu_item}>Duvidas</li>
        <li className={styles.menu_item}>Contato</li>
        <li className={styles.menu_item}>Configurações</li>
      </ul>
    </nav>
  );
};

export default Menu;
