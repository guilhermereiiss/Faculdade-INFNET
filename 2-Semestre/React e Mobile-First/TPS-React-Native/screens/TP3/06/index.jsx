import { useEffect, useState } from 'react';
import { StyleSheet, View, FlatList, ActivityIndicator } from 'react-native';
import ProdutoCard from './components/ProdutoCard.jsx';

export default function App() {
  const [produtos, setProdutos] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchProdutos();
  }, []);

  const fetchProdutos = async () => {
    try {
      const response = await fetch('https://dfef-dmrn-tps-default-rtdb.firebaseio.com/products.json');
      const data = await response.json();
      const produtosArray = Object.keys(data).map(key => ({
        id: key,
        ...data[key],
      }));
      setProdutos(produtosArray);
    } catch (error) {
      console.error('Erro ao buscar produtos:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator size="large" color="#0000ff" />
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <FlatList
        data={produtos}
        keyExtractor={item => item.id}
        renderItem={({ item }) => <ProdutoCard produto={item} />}
        contentContainerStyle={styles.list}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    padding: 10,
  },
  list: {
    paddingBottom: 10,
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});
