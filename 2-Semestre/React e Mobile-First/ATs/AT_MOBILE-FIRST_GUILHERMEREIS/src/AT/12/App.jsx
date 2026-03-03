
import Compras from "./Compras.jsx"

const App = () => {
  const itens = [
    { nome: 'Item 1', valorUnitario: 57.0, quantidade: 2 },
    { nome: 'Item 2', valorUnitario: 20.9, quantidade: 1 },
    { nome: 'Item 3', valorUnitario: 63.5, quantidade: 3 },
  ];

  return <Compras itens={itens} />;
};

export default App;


  