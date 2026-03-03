
import { View, Text, StyleSheet, Image, TouchableOpacity } from 'react-native';
import Icon from 'react-native-vector-icons/MaterialIcons';

export default function Perfil() {
  return (
    <View style={styles.container}>
      {/* Imagem de Perfil */}
      <Image 
        source={{ uri: 'https://via.placeholder.com/100' }}
        style={styles.profileImage}
      />
      
      
      <Text style={styles.userName}>João da Silva</Text>
      
      
      <Text style={styles.bio}>Aventureiro, fotógrafo e amante de viagens!</Text>
      
      {/* Informações do Perfil */}
      <View style={styles.infoContainer}>
        <View style={styles.infoBox}>
          <Text style={styles.infoNumber}>150</Text>
          <Text style={styles.infoText}>Viagens</Text>
        </View>
        <View style={styles.infoBox}>
          <Text style={styles.infoNumber}>300</Text>
          <Text style={styles.infoText}>Amigos</Text>
        </View>
      </View>
      
      {/* Ícones de Redes Sociais */}
      <View style={styles.socialMedia}>
        <TouchableOpacity>
          <Icon name="facebook" size={30} color="#3b5998" />
        </TouchableOpacity>
        <TouchableOpacity>
          <Icon name="instagram" size={30} color="#C13584" />
        </TouchableOpacity>
        <TouchableOpacity>
          <Icon name="twitter" size={30} color="#1DA1F2" />
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    backgroundColor: '#f0f0f0',
    padding: 20,
  },
  profileImage: {
    width: 100,
    height: 100,
    borderRadius: 50,
    marginBottom: 15,
  },
  userName: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
  },
  bio: {
    fontSize: 16,
    color: '#777',
    marginVertical: 10,
    textAlign: 'center',
  },
  infoContainer: {
    flexDirection: 'row',
    marginVertical: 20,
    width: '80%',
    justifyContent: 'space-around',
  },
  infoBox: {
    alignItems: 'center',
  },
  infoNumber: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#333',
  },
  infoText: {
    fontSize: 14,
    color: '#777',
  },
  socialMedia: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    width: '60%',
    marginTop: 20,
  },
});
