import Header from './components/header';
import GlobalMenu from './components/menuGlobal';
import ContextMenu from './components/contextMenu';
import MainContent from './components/mainContext';
import Ads from './components/ads';
import Footer from './components/footer';

import styles from "./grid.module.css";

function App() {
  return (
    <div className={styles.container}>
      <Header />
      <GlobalMenu />
      <ContextMenu />
      <MainContent />
      <Ads />
      <Footer />
    </div>
  );
}

export default App;
