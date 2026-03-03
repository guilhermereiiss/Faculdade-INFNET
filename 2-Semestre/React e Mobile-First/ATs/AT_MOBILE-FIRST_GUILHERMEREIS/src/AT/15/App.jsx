import Header from "./Components/Header/Header"

import MainMenu from './Components/Menu/Menu'
import Feed from "./Components/Feed/Feed"
import ListaAmigos from "./Components/Amigos/ListaAmigos";
import SugestaoAmigos from "./Components/Amigos/SugestaoAmigos";

const amigoData = [
  { id: 1, nome: "Maria Oliveira", foto: "/images/maria.png", amigosEmComum: 3 },
  { id: 2, nome: "Pedro Santos", foto: "/images/pedro.png", amigosEmComum: 2 },
];

const sugestoesData = [
  { id: 1, nome: "Ana Costa", foto: "/images/ana.png", amigosEmComum: "João Silva" },
  { id: 2, nome: "Carlos Almeida", foto: "/images/carlos.png", amigosEmComum: "Maria Oliveira" },
  
];

export default function App() {
  return (
    <>
      <Header />
      <MainMenu />
      <Feed />
      <ListaAmigos  amigos={amigoData}/>
      <SugestaoAmigos sugestoes={sugestoesData}/>
    </>
  );
}

