import { useState } from 'react';
import { View, TextInput, Button, StyleSheet } from 'react-native';

export default function Filtro({ onFiltrar }) {
  const [texto, setTexto] = useState('');

  return (
    <View style={styles.filtroContainer}>
      <TextInput
        style={styles.input}
        placeholder="Filtrar por nome ou descrição"
        value={texto}
        onChangeText={setTexto}
      />
      <Button title="Filtrar" onPress={() => onFiltrar(texto)} />
    </View>
  );
}

const styles = StyleSheet.create({
  filtroContainer: {
    marginBottom: 10,
  },
  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 8,
    marginBottom: 5,
  },
});
