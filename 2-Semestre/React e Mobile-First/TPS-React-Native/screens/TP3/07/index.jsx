
import  { useState } from 'react';
import { View, StyleSheet } from 'react-native';
import Filtro from './Filtro.jsx';
import ProdutoLista from './ProdutoLista.jsx';

const produtosData = [
  { id: '1', nome: 'Camiseta' },
  { id: '2', nome: 'Tênis' },
  { id: '3', nome: 'Boné' },
  { id: '4', nome: 'Calça Jeans' },
  { id: '5', nome: 'Jaqueta' },
];

export default function App() {
  const [produtos, setProdutos] = useState(produtosData);

  const filtrarProdutos = (texto) => {
    const filtrados = produtosData.filter(produto =>
      produto.nome.toLowerCase().includes(texto.toLowerCase())
    );
    setProdutos(filtrados);
  };

  return (
    <View style={styles.container}>
      <Filtro onFiltrar={filtrarProdutos} />
      <ProdutoLista produtos={produtos} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    padding: 16,
  },
});
