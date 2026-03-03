
import { FlatList, Text, View, StyleSheet } from 'react-native';

const Lista = ({ itens }) => {
  const renderItem = ({ item }) => (
    <View style={styles.item}>
      <Text style={styles.texto}>{item.nome}</Text>
    </View>
  );

  return (
    <FlatList
      data={itens}
      keyExtractor={(item) => item.id}
      renderItem={renderItem}
      contentContainerStyle={styles.listContainer}
    />
  );
};

const styles = StyleSheet.create({
  listContainer: {
    paddingVertical: 10,
  },
  item: {
    backgroundColor: '#fff',
    padding: 15,
    marginVertical: 8,
    borderRadius: 8,
    elevation: 3,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 4,
  },
  texto: {
    fontSize: 16,
    color: '#333',
  },
});

export default Lista;
