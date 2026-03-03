import Menu from "./components/Menu/Menu"
import TópicoPrincipal from "./components/Topicos/Topicos";
import ListaContribuições from "./components/Contribuições/ListaContribuições";
import FormResposta from "./components/Form/Formulario";
import RecenteTopico from "./components/Recentes/Recentes"

import "./main.css"


function App() {
    const topico = {
        titulo: "Tópico Principal do Fórum",
        subtitulo: "Discussão importante sobre React",
        descricao: "Neste tópico, discutimos práticas para criar aplicações em React...",
        autor: "BIG MIKE",
        data: "22/09/2024",
        curtidas: 120,
        respostas: 35,
    };

    const contribuicoes = [
        { autor: "Maria", data: "23/09/2024", resposta: "Ótima explicação!", curtidas: 10 },
        { autor: "Carlos", data: "23/09/2024", resposta: "Eu discordo de alguns pontos...", curtidas: 5 },
        { autor: "Marcos", data: "24/09/2024", resposta: "Eu faço mais melhor, pois....", curtidas: 1000 },
        { autor: "Lucas", data: "24/09/2024", resposta: "Eu penso diferente no sentido....", curtidas: 200 },
        { autor: "Guilherme", data: "24/09/2024", resposta: "Eu sabo isso...", curtidas: 1320 },
    ];

    const recentes = ["Gustavo Lima Preso", "Jeiel passou em Java", "Marcos descobriu uma nova especie", "Guilherme inventou a Matrix", "Alexandre fugiu de Minas Gerais "];
    const respondidos = ["Guilherme inventou a Matrix", "Marcos descobriu uma nova especie", "Gustavo Lima Preso", "Alexandre fugiu de Minas Gerais ", "Jeiel passou em Java"];
    const curtidos = ["Guilherme inventou a Matrix", "Marcos descobriu uma nova especie", "Gustavo Lima Preso", "Alexandre fugiu de Minas Gerais ", "Jeiel passou em Java"];

    return (
        <div>
            <Menu />
            <TópicoPrincipal {...topico} />
            <ListaContribuições contribuições={contribuicoes} />
            <FormResposta usuario="Josef" />
            <div className="some">
                <RecenteTopico recentes={recentes} respondidos={respondidos} curtidos={curtidos} />
            </div>
        </div>
    );
}

export default App;