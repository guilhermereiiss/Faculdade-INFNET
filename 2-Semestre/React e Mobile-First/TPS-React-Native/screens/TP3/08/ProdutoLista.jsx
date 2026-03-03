
import { FlatList, Text, View, StyleSheet } from 'react-native';

export default function ProdutoLista({ produtos }) {
  return (
    <FlatList
      data={produtos}
      keyExtractor={(item) => item.id}
      renderItem={({ item }) => (
        <View style={styles.itemContainer}>
          <Text style={styles.nome}>{item.nome}</Text>
          <Text style={styles.descricao}>{item.descricao}</Text>
        </View>
      )}
    />
  );
}

const styles = StyleSheet.create({
  itemContainer: {
    padding: 10,
    borderBottomWidth: 1,
    borderColor: '#ddd',
  },
  nome: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  descricao: {
    fontSize: 14,
    color: '#666',
  },
});
