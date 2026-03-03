

import { TouchableOpacity, Image, Text, StyleSheet } from 'react-native';

const ImageCard = ({ item, onPress }) => {
  const imageUrl = item.links?.[0]?.href;
  return (
    <TouchableOpacity style={styles.card} onPress={onPress}>
      <Image source={{ uri: imageUrl }} style={styles.image} />
      <Text style={styles.title}>{item.data[0].title}</Text>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  card: {
    margin: 10,
    backgroundColor: '#05070D',  
    borderRadius: 10,  
    padding: 10,  
    elevation: 5,  
  },
  image: {
    height: 150,
    borderRadius: 8,  
    width: '100%',  
  },
  title: {
    marginTop: 5,
    fontSize: 18,
    color: '#FFFF',  
    fontWeight: 'bold',  
  },
});

export default ImageCard;
