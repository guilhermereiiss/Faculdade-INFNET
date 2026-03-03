
import { View, FlatList, StyleSheet } from 'react-native';
import CarouselItem from './CarroselItem.jsx';

const images = [
  { id: '1', uri: 'https://i.pinimg.com/564x/f9/39/26/f939265d72f9461e70a0388e2c5a1279.jpg' },
  { id: '2', uri: 'https://i.pinimg.com/236x/c2/c7/88/c2c788ccbfba1850e2f68f7dedfc7c6f.jpg' },
  { id: '3', uri: 'https://i.pinimg.com/236x/09/f2/ee/09f2eee33935afcb491798ed04dc382a.jpg' },
  { id: '4', uri: 'https://i.pinimg.com/236x/d3/ba/02/d3ba028892688b76bc7e834ac1814855.jpg' },
];

export default function ImageCarousel() {
  return (
    <View style={styles.carouselContainer}>
      <FlatList
        data={images}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => <CarouselItem uri={item.uri} />}
        horizontal
        showsHorizontalScrollIndicator={false}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  carouselContainer: {
    display: 'flex',
    wrap: 'wrap',
    justifyContent: 'center',
    alignItems: 'center',
    paddingVertical: 20,
  },
});
