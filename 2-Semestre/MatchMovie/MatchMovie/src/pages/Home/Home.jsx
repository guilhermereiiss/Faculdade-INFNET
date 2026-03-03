
import Header from "../../components/Header/Header"
import Footer from "../../components/Footer/Footer"
import styles from "./Home.module.css"
import FilmesGerais from "../../Filmes/Filmes"

export default function Home() {
    return (
        <div className={styles.home}>
            <div>
                <Header />
                <div className={styles.home_content}>
                    <div>
                        <h2>SEJA BEM VINDO</h2>
                        <p>Descubra os melhores filmes e séries de todos os tempos</p>
                    </div>
                    <FilmesGerais/>
                </div>
                <Footer />
            </div>
        </div>
    )
}