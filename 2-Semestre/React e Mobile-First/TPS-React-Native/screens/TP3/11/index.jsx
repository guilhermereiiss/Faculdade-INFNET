import { useState, useEffect } from 'react';
import { View, StyleSheet } from 'react-native';
import ListaProdutos from './ListaProdutos';
import OrdenarProdutos from './OrdenarProdutos';

export default function App() {
  const [criterioOrdenacao, setCriterioOrdenacao] = useState('nome-asc');
  const [produtos, setProdutos] = useState([]);
  const [carregando, setCarregando] = useState(true);


  useEffect(() => {
    setTimeout(() => {
      const dadosProdutos = [
        { id: '1', nome: 'Café', preco: 5.0 },
        { id: '2', nome: 'Açúcar', preco: 3.5 },
        { id: '3', nome: 'Leite', preco: 4.0 },
        { id: '4', nome: 'Pão', preco: 2.5 },
      ];
      setProdutos(dadosProdutos);
      setCarregando(false);
    }, 2000);
  }, []);

  return (
    <View style={styles.container}>
      <OrdenarProdutos setCriterioOrdenacao={setCriterioOrdenacao} />
      <ListaProdutos produtos={produtos} criterioOrdenacao={criterioOrdenacao} carregando={carregando} />
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
