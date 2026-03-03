
import React from 'react';
import { View, StyleSheet } from 'react-native';
import ListaBase from './ListaBase';

export default function App() {
  const dados = [
    { id: 1, nome: '1' },
    { id: 2, nome: '2' },
    { id: 3, nome: '3' },
    { id: 4, nome: '4' },
  ];

  return (
    <View style={estilos.container}>
      <ListaBase dados={dados} />
    </View>
  );
}

const estilos = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
    paddingTop: 50,
  },
});
