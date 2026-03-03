import { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

export default function App() {
  const [number, setNumber] = useState('');
  const [result, setResult] = useState('');

  const primew = (num) => {
    if (num <= 1) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return true;
  };

  const calculo = () => {
    const numeror = Number(number, 10);
    if (!isNaN(numeror)) {
      setResult(primew(numeror) ? 'É primo' : 'Não é primo');
    } else {
      setResult('Por favor, insira um número válido.');
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Verificar Número Primo</Text>
      <TextInput
        style={styles.input}
        placeholder="Digite um número"
        keyboardType="numeric"
        value={number}
        onChangeText={(text) => setNumber(text)}
      />
      <Button title="Verificar" onPress={calculo} />
      {result ? <Text style={styles.result}>{result}</Text> : null}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
    backgroundColor: '#f0f0f0',
  },
  title: {
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
  result: {
    fontSize: 20,
    marginTop: 20,
    color: '#333',
  },
});
