
import { View, Text, StyleSheet, FlatList } from 'react-native';

const ListaEspacada = ({ data }) => {
  return (
    <FlatList
      data={data}
      keyExtractor={(item) => item.id.toString()}
      contentContainerStyle={styles.listContainer}
      renderItem={({ item }) => (
        <View style={styles.itemContainer}>
          <Text style={styles.itemText}>{item.name}</Text>
        </View>
      )}
    />
  );
};

const styles = StyleSheet.create({
  listContainer: {
    flexGrow: 1,
    justifyContent: 'space-between',
    paddingVertical: 20,
  },
  itemContainer: {
    padding: 15,
    backgroundColor: '#333',
    borderRadius: 10,
    marginHorizontal: 20,
    alignItems: 'center',
  },
  itemText: {
    fontSize: 18,
    color: 'white',
  },
});

export default ListaEspacada;
