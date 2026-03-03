
import { View, Image, StyleSheet } from 'react-native';

export default function GridItem({ uri }) {
  return (
    <View style={styles.itemContainer}>
      <Image source={{ uri }} style={styles.image} />
    </View>
  );
}

const styles = StyleSheet.create({
  itemContainer: {
    flex: 1,
    margin: 5,
    width: 100,
    height: 100,
    borderRadius: 10,
    overflow: 'hidden',
  },
  image: {
    width: '100%',
    height: '100%',
    resizeMode: 'cover',
  },
});
