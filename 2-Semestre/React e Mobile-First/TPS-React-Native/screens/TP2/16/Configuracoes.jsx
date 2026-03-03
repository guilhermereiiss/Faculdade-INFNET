import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet, FlatList } from 'react-native';
import Icon from 'react-native-vector-icons/MaterialIcons';

const configuracoes = [
  { id: '1', titulo: 'Conta', icone: 'person' },
  { id: '2', titulo: 'Notificações', icone: 'notifications' },
  { id: '3', titulo: 'Privacidade', icone: 'lock' },
  { id: '4', titulo: 'Tema', icone: 'color-lens' },
  { id: '5', titulo: 'Sobre', icone: 'info' },
];

export default function Configuracoes() {
  return (
    <View style={styles.container}>
      <Text style={styles.titulo}>Configurações</Text>
      <FlatList
        data={configuracoes}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <TouchableOpacity style={styles.configItem}>
            <Icon name={item.icone} size={24} color="#555" style={styles.icon} />
            <Text style={styles.configText}>{item.titulo}</Text>
            <Icon name="chevron-right" size={24} color="#555" />
          </TouchableOpacity>
        )}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f7f7f7',
  },
  titulo: {
    fontSize: 26,
    fontWeight: 'bold',
    margin: 20,
    color: '#333',
    textAlign: 'center',
  },
  configItem: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 15,
    paddingHorizontal: 20,
    borderBottomWidth: 1,
    borderBottomColor: '#ddd',
  },
  configText: {
    fontSize: 18,
    color: '#333',
    flex: 1,
    marginLeft: 10,
  },
  icon: {
    marginRight: 15,
  },
});
