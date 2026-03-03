import { useState } from 'react';
import { View, StyleSheet } from 'react-native';
import ListaProdutos from './ListaProdutos';
import OrdenarProdutos from './OrdenarProdutos';

export default function App() {
  const [criterioOrdenacao, setCriterioOrdenacao] = useState('nome-asc'); // Padrão

  const produtos = [
    { id: '1', nome: 'Café', preco: 5.0 },
    { id: '2', nome: 'Açúcar', preco: 3.5 },
    { id: '3', nome: 'Leite', preco: 4.0 },
    { id: '4', nome: 'Pão', preco: 2.5 },
  ];

  return (
    <View style={styles.container}>
      <OrdenarProdutos setCriterioOrdenacao={setCriterioOrdenacao} />
      <ListaProdutos produtos={produtos} criterioOrdenacao={criterioOrdenacao} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: 50,
    backgroundColor: '#f0f0f0',
  },
});
