import  { useState } from 'react';
import { View, StyleSheet } from 'react-native';
import Filtro from './Filtro';
import ProdutoLista from './ProdutoLista';

const produtosData = [
  { id: '1', nome: 'Camiseta', descricao: 'Camiseta de algodão branca' },
  { id: '2', nome: 'Tênis', descricao: 'Tênis esportivo confortável' },
  { id: '3', nome: 'Boné', descricao: 'Boné ajustável preto' },
  { id: '4', nome: 'Calça Jeans', descricao: 'Calça jeans azul escura' },
  { id: '5', nome: 'Jaqueta', descricao: 'Jaqueta de couro sintético' },
];

export default function App() {
  const [produtos, setProdutos] = useState(produtosData);

  const filtrarProdutos = (texto) => {
    const filtrados = produtosData.filter(produto =>
      produto.nome.toLowerCase().includes(texto.toLowerCase()) ||
      produto.descricao.toLowerCase().includes(texto.toLowerCase())
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
