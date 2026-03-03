import Header from "../../Components/Header/header.jsx"
import "./home.css"
import Hoteis from "../../Components/Hoteis/hoteis.jsx"



export default function Home() {
   
    return (
        <div className="home">
            <div>
                <Header />
                <div className="home_content">
                    <h2>CONHEÇAS OS MELHORES HOTEIS DO BRASIL</h2>
                    <Hoteis />
                </div>
            </div>
        </div>
    )
}