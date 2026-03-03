import Header from "./components/Header/Header"
import dados from './dados';
import DetalhesProduto from "./components/Detalhes/DetalhesProduto";
import Vendedor from "./components/Vendedor/Vendedor"
import Comentarios from "./components/Comentarios/Comentarios"
import Perguntas from "./components/Perguntas/Perguntas";
import Produtos from "./components/Produtos/Produtos"

const App = () => {
    const { produto, vendedor, comentarios,perguntas,produtosRelacionados } = dados

    

    return (
        <div className="app">
            <Header />
            <main>
                <DetalhesProduto produto={produto} />
                 <Vendedor vendedor={vendedor} />
                 <Comentarios comentarios={comentarios} />
                <Perguntas perguntas={perguntas} />
             <Produtos produtos={produtosRelacionados} />
            </main>
        </div>
    );
};

export default App;