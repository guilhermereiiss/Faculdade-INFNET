import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

export default function App() {
  const [texto, setTexto] = useState('');
  const [resultado, setResultado] = useState('');

  const verificarPalindromo = () => {
    const textoLimpo = texto.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
    const textoInvertido = textoLimpo.split('').reverse().join('');
    setResultado(textoLimpo === textoInvertido ? 'É um palíndromo' : 'Não é um palíndromo');
  };

  return (
    <View style={estilos.container}>
      <Text style={estilos.titulo}>Verificar Palíndromo</Text>
      <TextInput
        style={estilos.input}
        placeholder="Digite uma palavra ou frase"
        value={texto}
        onChangeText={(texto) => setTexto(texto)}
      />
      <Button title="Verificar" onPress={verificarPalindromo} />
      {resultado ? <Text style={estilos.resultado}>{resultado}</Text> : null}
    </View>
  );
}

const estilos = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
    backgroundColor: '#f0f0f0',
  },
  titulo: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  input: {
    width: '80%',
    padding: 10,
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 5,
    marginBottom: 10,
    fontSize: 18,
  },
  resultado: {
    fontSize: 20,
    marginTop: 20,
    color: '#333',
  },
});
