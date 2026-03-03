import { useState } from 'react';
import styles from './Menu.module.css';
import MinhaLogo from "./MINHALOGO.jpeg";

const Menu = () => {
    const [menuAberto, setMenuAberto] = useState(false);

    const alternarMenu = () => {
        setMenuAberto(!menuAberto);
    };

    return (
        <nav className={`${styles.menu} ${menuAberto ? styles.aberto : ''}`}>
            <div className={styles.menu_topo}>
                <img src={MinhaLogo} alt="Logo" className={styles.menu_logo} />
                <button className={styles.menu_botao} onClick={alternarMenu}>
                    &#9776;
                </button>
                <h1>CallChan</h1>
            </div>
            <ul className={`${styles.menu_lista} ${menuAberto ? styles.visivel : ''}`}>
                <li className={styles.menu_item}>Perfil</li>
                <li className={styles.menu_item}>Postagens</li>
                <li className={styles.menu_item}>Amigos</li>
                <li className={styles.menu_item}>Populares</li>
                <li className={styles.menu_item}>Recomendados</li>
            </ul>
        </nav>
    );
};

export default Menu;
