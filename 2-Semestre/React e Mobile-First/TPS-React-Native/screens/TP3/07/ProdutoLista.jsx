
import { FlatList, Text, View, StyleSheet } from 'react-native';

export default function ProdutoLista({ produtos }) {
  return (
    <FlatList
      data={produtos}
      keyExtractor={(item) => item.id}
      renderItem={({ item }) => (
        <View style={styles.itemContainer}>
          <Text style={styles.text}>{item.nome}</Text>
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
  text: {
    fontSize: 18,
  },
});
