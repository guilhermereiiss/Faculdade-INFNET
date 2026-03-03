
import { View, Text, Image, StyleSheet } from 'react-native';

const ContatoItem = ({ avatar, nome, endereco, numero }) => {
  return (
    <View style={estilos.contatoContainer}>
      <Image source={{ uri: avatar }} style={estilos.avatar} />
      <View style={estilos.infoContainer}>
        <Text style={estilos.nome}>{nome}</Text>
        <Text style={estilos.endereco}>{endereco}</Text>
        <Text style={estilos.numero}>{numero}</Text>
      </View>
    </View>
  );
};

const estilos = StyleSheet.create({
  contatoContainer: {
    flexDirection: 'row',
    padding: 15,
    borderBottomWidth: 1,
    borderBottomColor: '#ccc',
    alignItems: 'center',
  },
  avatar: {
    width: 50,
    height: 50,
    borderRadius: 25,
    marginRight: 15,
  },
  infoContainer: {
    flex: 1,
  },
  nome: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
  },
  endereco: {
    fontSize: 14,
    color: '#666',
  },
  numero: {
    fontSize: 14,
    color: '#666',
  },
});

export default ContatoItem;
