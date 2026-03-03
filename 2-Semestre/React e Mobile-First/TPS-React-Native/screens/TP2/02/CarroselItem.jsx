
import { View, Image, StyleSheet } from 'react-native';

export default function CarouselItem({ uri }) {
  return (
    <View style={styles.itemContainer}>
      <Image source={{ uri }} style={styles.image} />
    </View>
  );
}

const styles = StyleSheet.create({
  itemContainer: {
    width: 50,
    height: 50,
    marginHorizontal: 10,
    borderRadius: 10,
    overflow: 'hidden',
  },
  image: {
    width: '100%',
    height: '100%',
    resizeMode: 'cover',
  },
});
