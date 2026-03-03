
import { View, Text, StyleSheet, FlatList } from 'react-native';

const EsquerdaLista = ({ data }) => {
  return (
    <FlatList
      data={data}
      keyExtractor={(item) => item.id.toString()}
      renderItem={({ item }) => (
        <View style={styles.itemContainer}>
          <Text style={styles.itemText}>{item.name}</Text>
        </View>
      )}
    />
  );
};

const styles = StyleSheet.create({
  itemContainer: {
    flexDirection: 'row',
    justifyContent: 'flex-start',
    padding: 15,
  },
  itemText: {
    fontSize: 16,
    textAlign: 'right',
  },
});

export default EsquerdaLista;
