
import React from 'react';
import { View, Text, StyleSheet, FlatList } from 'react-native';

const ListaBase = ({ dados }) => {
  return (
    <FlatList
      data={dados}
      keyExtractor={(item) => item.id.toString()}
      contentContainerStyle={estilos.listaContainer}
      renderItem={({ item }) => (
        <View style={estilos.itemContainer}>
          <Text style={estilos.itemTexto}>{item.nome}</Text>
        </View>
      )}
    />
  );
};

const estilos = StyleSheet.create({
  listaContainer: {
    flexGrow: 1,
    justifyContent: 'flex-end',
    paddingVertical: 20,
  },
  itemContainer: {
    padding: 15,
    backgroundColor: '#e0e0e0',
    borderRadius: 10,
    marginHorizontal: 20,
    marginBottom: 10,
    alignItems: 'center',
  },
  itemTexto: {
    fontSize: 18,
    color: '#333',
  },
});

export default ListaBase;
