
import { FlatList, Text, View, StyleSheet, ActivityIndicator } from 'react-native';

export default function ListaProdutos({ produtos, criterioOrdenacao, carregando }) {
  if (carregando) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator size="large" color="#0000ff" />
        <Text>Carregando...</Text>
      </View>
    );
  }

  const produtosOrdenados = [...produtos].sort((a, b) => {
    switch (criterioOrdenacao) {
      case 'nome-asc':
        return a.nome.localeCompare(b.nome);
      case 'nome-desc':
        return b.nome.localeCompare(a.nome);
      case 'preco-asc':
        return a.preco - b.preco;
      case 'preco-desc':
        return b.preco - a.preco;
      default:
        return 0;
    }
  });

  return (
    <FlatList
      data={produtosOrdenados}
      keyExtractor={(item) => item.id}
      renderItem={({ item }) => (
        <View style={styles.item}>
          <Text style={styles.nome}>{item.nome}</Text>
          <Text style={styles.preco}>R$ {item.preco.toFixed(2)}</Text>
        </View>
      )}
    />
  );
}

const styles = StyleSheet.create({
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  item: {
    padding: 15,
    borderBottomWidth: 1,
    borderColor: '#ccc',
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  nome: {
    fontSize: 18,
  },
  preco: {
    fontSize: 16,
    color: '#666',
  },
});
