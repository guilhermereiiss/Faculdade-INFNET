import { useState } from "react";
import styles from "./grid.module.css";

function App() {
  const [menuAberto, setMenuAberto] = useState(false);

  const toggleMenu = () => {
    setMenuAberto(!menuAberto);
  };

  return (
    <div className={styles.container}>
      <header>Header</header>
      <main>

        <button onClick={toggleMenu} style={{ cursor: 'pointer' }}>
          {menuAberto ? '−' : '☰'} 
        </button>
        Global Menu
        {menuAberto && (
          <nav className={styles.menu}>
            <ul>
              <li>ITEM 1</li>
              <li>ITEM 2</li>
              <li>ITEM 3</li>
              <li>ITEM 4</li>
              <li>ITEM 5</li>
            </ul>
          </nav>
        )}
      </main>
      <article>Context Menu</article>
      <section>Main Content</section>
      <aside>Ads</aside>
      <footer>Footer</footer>
    </div>
  );
}

export default App;
