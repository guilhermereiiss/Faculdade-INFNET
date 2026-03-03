
import { View, FlatList, StyleSheet } from 'react-native';
import GridItem from './GridItem.jsx';

const images = [
    { id: '1', uri: 'https://i.pinimg.com/564x/f9/39/26/f939265d72f9461e70a0388e2c5a1279.jpg' },
    { id: '2', uri: 'https://i.pinimg.com/236x/c2/c7/88/c2c788ccbfba1850e2f68f7dedfc7c6f.jpg' },
    { id: '3', uri: 'https://i.pinimg.com/236x/09/f2/ee/09f2eee33935afcb491798ed04dc382a.jpg' },
    { id: '4', uri: 'https://i.pinimg.com/236x/d3/ba/02/d3ba028892688b76bc7e834ac1814855.jpg' },
  ];

export default function ImageGrid() {
  return (
    <View style={styles.gridContainer}>
      <FlatList
        data={images}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => <GridItem uri={item.uri} />}
        numColumns={2} // Define o número de colunas da grade
        showsVerticalScrollIndicator={false}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  gridContainer: {
    flex: 1,
    paddingHorizontal: 10,
  },
});
