import { FlatList, Text, View, StyleSheet } from 'react-native';

export default function ListaProdutos({ produtos, ordenacao }) {
  const produtosOrdenados = [...produtos].sort((a, b) => {
    if (ordenacao === 'asc') {
      return a.nome.localeCompare(b.nome);
    } else {
      return b.nome.localeCompare(a.nome);
    }
  });

  return (
    <FlatList
      data={produtosOrdenados}
      keyExtractor={(item) => item.id}
      renderItem={({ item }) => (
        <View style={styles.item}>
          <Text>{item.nome}</Text>
        </View>
      )}
    />
  );
}

const styles = StyleSheet.create({
  item: {
    padding: 15,
    borderBottomWidth: 1,
    borderColor: '#ccc',
  },
});