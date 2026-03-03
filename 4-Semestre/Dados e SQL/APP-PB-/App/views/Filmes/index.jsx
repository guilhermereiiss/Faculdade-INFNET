import { useEffect, useState } from 'react';
import { View, Text, FlatList, Image, TouchableOpacity, StyleSheet, Modal, Button, TextInput, Platform } from 'react-native';
import axios from 'axios';
import { Ionicons } from '@expo/vector-icons';
import AsyncStorage from '@react-native-async-storage/async-storage';

export default function ListaFilmes({ navigation }) {
  const [filmes, setFilmes] = useState([]);
  const [filmesFiltrados, setFilmesFiltrados] = useState([]);
  const [pagina, setPagina] = useState(1);
  const [carregando, setCarregando] = useState(false);
  const [favoritos, setFavoritos] = useState([]);
  const [modalVisible, setModalVisible] = useState(false);
  const [filmeSelecionado, setFilmeSelecionado] = useState(null);
  const [elenco, setElenco] = useState([]);
  const [pesquisa, setPesquisa] = useState('');

  const fetchFilmes = async (paginaAtual) => {
    if (carregando) return;
    setCarregando(true);
    const response = await axios.get(`https://api.themoviedb.org/3/movie/popular?api_key=12374ecb147586c8d10ec01440db879d&language=pt-BR&page=${paginaAtual}`);
    setFilmes((prev) => [...prev, ...response.data.results]);
    setCarregando(false);
  };

  const fetchDetalhesFilme = async (id) => {
    const detalhesResponse = await axios.get(`https://api.themoviedb.org/3/movie/${id}?api_key=12374ecb147586c8d10ec01440db879d&language=pt-BR`);
    const elencoResponse = await axios.get(`https://api.themoviedb.org/3/movie/${id}/credits?api_key=12374ecb147586c8d10ec01440db879d&language=pt-BR`);

    setFilmeSelecionado(detalhesResponse.data);
    setElenco(elencoResponse.data.cast);
    setModalVisible(true);
  };

  const loadFavoritos = async () => {
    try {
      const favoritosSalvos = await AsyncStorage.getItem('favoritos');
      if (favoritosSalvos) {
        setFavoritos(JSON.parse(favoritosSalvos));
      }
    } catch (error) {
      console.error("Erro ao carregar favoritos", error);
    }
  };

  const toggleFavorito = async (id) => {
    let novosFavoritos;
    if (favoritos.includes(id)) {
      novosFavoritos = favoritos.filter((item) => item !== id);
    } else {
      novosFavoritos = [...favoritos, id];
    }
    setFavoritos(novosFavoritos);
    await AsyncStorage.setItem('favoritos', JSON.stringify(novosFavoritos));
  };

  const handlePesquisa = (texto) => {
    setPesquisa(texto);
    if (texto === '') {
      setFilmesFiltrados(filmes);
    } else {
      const filmesResultado = filmes.filter(filme =>
        filme.title.toLowerCase().includes(texto.toLowerCase())
      );
      setFilmesFiltrados(filmesResultado);
    }
  };

  useEffect(() => {
    fetchFilmes(pagina);
    loadFavoritos();
  }, [pagina]);

  useEffect(() => {
    setFilmesFiltrados(filmes);
  }, [filmes]);

  const carregarMaisFilmes = () => {
    setPagina((prevPagina) => prevPagina + 1);
  };

  const abrirDetalhes = (item) => {
    fetchDetalhesFilme(item.id);
  };

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.inputPesquisa}
        placeholder="Buscar filmes..."
        placeholderTextColor="#aaa"
        value={pesquisa}
        onChangeText={handlePesquisa}
      />

      <FlatList
        data={filmesFiltrados}
        keyExtractor={(item) => item.id.toString()}
        numColumns={2}
        onEndReached={carregarMaisFilmes}
        onEndReachedThreshold={0.5}
        contentContainerStyle={styles.flatListContainer}
        renderItem={({ item }) => (
          <TouchableOpacity style={styles.card} onPress={() => abrirDetalhes(item)}>
            <Image source={{ uri: `https://image.tmdb.org/t/p/w500${item.poster_path}` }} style={styles.imagem} />
            <View style={styles.detalhes}>
              <Text style={styles.titulo} numberOfLines={2}>{item.title}</Text>
              <TouchableOpacity onPress={() => toggleFavorito(item.id)} style={styles.botaoFavorito}>
                <Ionicons
                  name={favoritos.includes(item.id) ? 'heart' : 'heart-outline'}
                  size={24}
                  color={favoritos.includes(item.id) ? '#D17FFF' : '#FFF'}
                />
              </TouchableOpacity>
            </View>
          </TouchableOpacity>
        )}
      />

      <Modal
        visible={modalVisible}
        animationType={Platform.OS === 'ios' ? 'slide' : 'fade'}
        onRequestClose={() => setModalVisible(false)}
      >
        <View style={styles.modalContainer}>
          {filmeSelecionado && (
            <>
              <Image
                source={{ uri: `https://image.tmdb.org/t/p/w500${filmeSelecionado.poster_path}` }}
                style={styles.imagemDetalhes}
              />
              <Text style={styles.tituloDetalhes}>{filmeSelecionado.title}</Text>
              <Text style={styles.ano}>{new Date(filmeSelecionado.release_date).getFullYear()}</Text>
              <Text style={styles.nota}>Nota: {filmeSelecionado.vote_average}/10</Text>
              <Text style={styles.descricao}>{filmeSelecionado.overview}</Text>
              <Text style={styles.elencoTitulo}>Elenco:</Text>
              <FlatList
                data={elenco.slice(0, 5)}
                keyExtractor={(item) => item.cast_id.toString()}
                renderItem={({ item }) => (
                  <Text style={styles.elencoNome}>{item.name}</Text>
                )}
              />
              <Button title="Fechar" onPress={() => setModalVisible(false)} />
            </>
          )}
        </View>
      </Modal>

      <TouchableOpacity
        style={styles.botaoFavoritos}
        onPress={() => navigation.navigate('Favoritos', { favoritos })}
      >
        <Text style={styles.textoBotaoFavoritos}>Seus Favoritos</Text>
      </TouchableOpacity>
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
  inputPesquisa: {
    height: 40,
    borderColor: '#9F2CBF',
    borderWidth: 1,
    borderRadius: 20,
    paddingLeft: 15,
    marginBottom: 10,
    color: '#FFF',
    fontSize: 16,
  },
  flatListContainer: {
    paddingBottom: 20,
  },
  card: {
    backgroundColor: '#281259',
    flex: 1,
    margin: 5,
    borderRadius: 12,
    overflow: 'hidden',
    shadowColor: '#FFF',
    shadowOpacity: 0.1,
    elevation: 4,
  },
  imagem: {
    width: '100%',
    height: 180,
  },
  detalhes: {
    padding: 10,
    alignItems: 'center',
  },
  titulo: {
    color: '#FFF',
    fontSize: 14,
    fontWeight: 'bold',
    textAlign: 'center',
  },
  botaoFavorito: {
    backgroundColor: '#9F2CBF',
    padding: 8,
    borderRadius: 50,
    marginTop: 10,
  },
  modalContainer: {
    flex: 1,
    backgroundColor: '#0b0e21',
    padding: 20,
    alignItems: 'center',
  },
  imagemDetalhes: {
    width: '100%',
    height: 300,
    borderRadius: 10,
  },
  tituloDetalhes: {
    color: '#FFF',
    fontSize: 22,
    fontWeight: 'bold',
    marginTop: 10,
  },
  ano: {
    color: '#FFF',
    fontSize: 18,
    marginTop: 5,
  },
  nota: {
    color: '#FFF',
    fontSize: 18,
    marginTop: 5,
  },
  descricao: {
    color: '#FFF',
    fontSize: 16,
    marginTop: 10,
    textAlign: 'justify',
  },
  elencoTitulo: {
    color: '#FFF',
    fontSize: 18,
    fontWeight: 'bold',
    marginTop: 10,
  },
  elencoNome: {
    color: '#FFF',
    fontSize: 16,
    marginTop: 5,
  },
  botaoFavoritos: {
    backgroundColor: '#9F2CBF',
    padding: 15,
    borderRadius: 10,
    marginTop: 20,
    alignItems: 'center',
  },
  textoBotaoFavoritos: {
    color: '#FFF',
    fontSize: 18,
    fontWeight: 'bold',
  },
});

