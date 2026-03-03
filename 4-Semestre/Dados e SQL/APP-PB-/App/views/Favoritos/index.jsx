import { useState, useEffect } from 'react';
import { View, Text, FlatList, Image, TouchableOpacity, StyleSheet, Platform } from 'react-native';
import axios from 'axios';

export default function FavoritosScreen({ route, navigation }) {
  const { favoritos } = route.params;
  const [filmesFavoritos, setFilmesFavoritos] = useState([]);

  useEffect(() => {
    const fetchFilmesFavoritos = async () => {
      const filmesDetalhes = await Promise.all(
        favoritos.map(async (id) => {
          const response = await axios.get(`https://api.themoviedb.org/3/movie/${id}?api_key=12374ecb147586c8d10ec01440db879d&language=pt-BR`);
          return response.data;
        })
      );
      setFilmesFavoritos(filmesDetalhes);
    };
    fetchFilmesFavoritos();
  }, [favoritos]);

  return (
    <View style={styles.container}>
      <FlatList
        data={filmesFavoritos}
        keyExtractor={(item) => item.id.toString()}
        numColumns={2}
        renderItem={({ item }) => (
          <TouchableOpacity style={styles.card} onPress={() => navigation.navigate('Detalhes', { id: item.id })}>
            <Image source={{ uri: `https://image.tmdb.org/t/p/w500${item.poster_path}` }} style={styles.imagem} />
            <Text style={styles.titulo} numberOfLines={2}>{item.title}</Text>
          </TouchableOpacity>
        )}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0b0e21',
    paddingVertical: 10,
    paddingHorizontal: 5,
  },
  card: {
    backgroundColor: '#281259',
    flex: 1,
    margin: 5,
    borderRadius: 12,
    overflow: 'hidden',
    shadowColor: Platform.OS === 'ios' ? '#FFF' : '#000', 
    shadowOpacity: Platform.OS === 'ios' ? 0.3 : 0.1,
    shadowRadius: 5,
    elevation: Platform.OS === 'android' ? 4 : 0, 
  },
  imagem: {
    width: '100%',
    height: 180,
  },
  titulo: {
    color: '#FFF',
    fontSize: 14,
    fontWeight: 'bold',
    textAlign: 'center',
    padding: 10,
  },
});
