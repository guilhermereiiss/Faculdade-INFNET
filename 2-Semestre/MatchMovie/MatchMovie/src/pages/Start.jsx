import { useNavigate } from "react-router-dom"
import "./start.css"

const Start = () => {
    const navigate = useNavigate();

    const navegaCentral = () => {
        navigate('/MatchMovie/login')
    }
    return (
        <div className='container'>
            <button onClick={navegaCentral} className='button'>Inicie o Projeto</button>
        </div>
    )
}

export default Start
