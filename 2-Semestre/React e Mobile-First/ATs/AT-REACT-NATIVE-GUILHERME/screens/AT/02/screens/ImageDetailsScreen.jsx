import { View, Image, Text, StyleSheet } from 'react-native';

const ImageDetailsScreen = ({ route }) => {
  const { item } = route.params;
  const imageUrl = item.links?.[0]?.href;

  return (
    <View style={styles.container}>
      <Image source={{ uri: imageUrl }} style={styles.image} />
      <Text style={styles.title}>{item.data[0].title}</Text>
      <Text style={styles.description}>{item.data[0].description}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#101526',  
    padding: 20,
  },
  image: {
    height: 300,
    borderRadius: 10,  
    marginBottom: 20,
  },
  title: {
    fontSize: 24,
    color: '#FFFF', 
    marginBottom: 10,
  },
  description: {
    fontSize: 16,
    color: '#FFFF',  
  },
});

export default ImageDetailsScreen;
