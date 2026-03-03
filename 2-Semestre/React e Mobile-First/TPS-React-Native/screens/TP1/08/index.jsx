
import { View, Text, Image, StyleSheet } from 'react-native';

const MovieCard = ({ title, cinema, time, image }) => {
  return (
    <View style={styles.card}>
      <Image source={{ uri: image }} style={styles.image} />
      <View style={styles.details}>
        <Text style={styles.title}>{title}</Text>
        <Text style={styles.info}>Cinema: {cinema}</Text>
        <Text style={styles.info}>Horário: {time}</Text>
      </View>
    </View>
  );
};

export default function App() {
  return (
    <View style={styles.container}>
      <MovieCard
        title="O Poço 2"
        cinema="Cinemark"
        time="18:30"
        image="https://canada1.discourse-cdn.com/ifood/original/2X/6/6bdb2bc493f5504c35455553082e6ac1d7c2c87f.jpeg"
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f0f0f0',
  },
  card: {
    width: 300,
    backgroundColor: '#fff',
    borderRadius: 10,
    overflow: 'hidden',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.8,
    shadowRadius: 2,
    elevation: 5,
  },
  image: {
    width: '100%',
    height: 180,
  },
  details: {
    padding: 10,
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 5,
  },
  info: {
    fontSize: 14,
    color: '#555',
  },
});
