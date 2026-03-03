import MinhaLogo from "./MINHALOGO.jpeg"
import Profile from "./icons8-usuário-homem-com-círculo-100.png"
import './main.css'

export default function App() {
    return (
        <header className="container_header">
            <img src={MinhaLogo} alt="logotipo" />
            <nav>
                <ul className="organiza_itens">
                    <li>Item </li>
                    <li>Item </li>
                    <li>Item </li>
                </ul>
            </nav>

            <img src={Profile} alt="perfil" className="profile_img" />
        </header>
    )
}