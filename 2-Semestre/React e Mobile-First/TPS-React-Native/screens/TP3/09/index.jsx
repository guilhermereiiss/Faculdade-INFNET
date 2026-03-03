import { useState } from 'react';
import { View, StyleSheet } from 'react-native';
import ListaProdutos from './ListaProdutos.jsx';
import OrdenarProdutos from './OrdenarProdutos.jsx';

export default function App() {
  const [ordenacao, setOrdenacao] = useState('asc'); 

  const produtos = [
    { id: '1', nome: 'Café' },
    { id: '2', nome: 'Açúcar' },
    { id: '3', nome: 'Leite' },
    { id: '4', nome: 'Pão' },
  ];

  return (
    <View style={styles.container}>
      <OrdenarProdutos setOrdenacao={setOrdenacao} />
      <ListaProdutos produtos={produtos} ordenacao={ordenacao} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    backgroundColor: '#fff',
  },
});
