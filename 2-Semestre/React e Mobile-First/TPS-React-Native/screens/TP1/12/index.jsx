import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

export default function App() {
  const [dataNascimento, setDataNascimento] = useState('');
  const [horaNascimento, setHoraNascimento] = useState('');
  const [resultado, setResultado] = useState('');

  const calcularIdade = () => {

    const [dia, mes, ano] = dataNascimento.split('/').map(Number);
    const [hora, minuto] = horaNascimento.split(':').map(Number);
    
    const dataNasc = new Date(ano, mes - 1, dia, hora, minuto);
    const agora = new Date();

    const diferenca = new Date(agora - dataNasc);

    const anos = diferenca.getUTCFullYear() - 1970;
    const meses = diferenca.getUTCMonth();
    const dias = diferenca.getUTCDate() - 1;
    const horas = diferenca.getUTCHours();
    const minutos = diferenca.getUTCMinutes();

    setResultado(`Idade: ${anos} anos, ${meses} meses, ${dias} dias, ${horas} horas e ${minutos} minutos.`);
  };

  return (
    <View style={estilos.container}>
      <Text style={estilos.titulo}>Calcular Idade</Text>
      <TextInput
        style={estilos.input}
        placeholder="Digite a data de nascimento (DD/MM/AAAA)"
        value={dataNascimento}
        onChangeText={setDataNascimento}
      />
      <TextInput
        style={estilos.input}
        placeholder="Digite a hora de nascimento (HH:MM)"
        value={horaNascimento}
        onChangeText={setHoraNascimento}
      />
      <Button title="Calcular Idade" onPress={calcularIdade} />
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
