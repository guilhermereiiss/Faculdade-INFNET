import ListaCompras from "./components/ListaCompras";

const itensDaCompra = [
  { nome: "PC Gamer", valorUnitario: 10000, quantidade: 2 },
  { nome: "Feijão", valorUnitario: 7.49, quantidade: 1 },
  { nome: "Carro", valorUnitario: 80000, quantidade: 4 },
];

function App() {
  return (
    <div>
      <ListaCompras itens={itensDaCompra} />
    </div>
  );
}

export default App;