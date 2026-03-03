
import { StyleSheet, View, Text, Image } from 'react-native';

export default function ProdutoCard({ produto }) {
  return (
    <View style={styles.card}>
      <Image source={{ uri: produto.imagens[0] }} style={styles.image} />
      <Text style={styles.nome}>{produto.nome}</Text>
      <Text style={styles.preco}>R$ {produto.preco.toFixed(2)}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: '#f9f9f9',
    borderRadius: 8,
    padding: 10,
    marginBottom: 10,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 2 },
    shadowRadius: 4,
    elevation: 2,
  },
  image: {
    width: '100%',
    height: 150,
    borderRadius: 8,
    marginBottom: 10,
  },
  nome: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 5,
  },
  preco: {
    fontSize: 14,
    color: '#555',
  },
});
