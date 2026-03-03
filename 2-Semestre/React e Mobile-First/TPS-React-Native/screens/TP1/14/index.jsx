import { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';

export default function App() {
  const [resultado, setResultado] = useState('');

  const adicionarValor = (valor) => {
    setResultado((prev) => prev + valor);
  };

  const calcularResultado = () => {
    try {
      const calculo = eval(resultado); 
      setResultado(String(calculo));
    } catch (error) {
      setResultado('Erro');
    }
  };

  const limpar = () => setResultado('');

  const criarBotao = (valor, estiloAdicional = {}) => (
    <TouchableOpacity
      style={[styles.botao, estiloAdicional]}
      onPress={() => adicionarValor(valor)}
    >
      <Text style={styles.textoBotao}>{valor}</Text>
    </TouchableOpacity>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.resultado}>{resultado}</Text>

      <View style={styles.linha}>
        {criarBotao('7')}
        {criarBotao('8')}
        {criarBotao('9')}
        {criarBotao('/', styles.operador)}
      </View>

      <View style={styles.linha}>
        {criarBotao('4')}
        {criarBotao('5')}
        {criarBotao('6')}
        {criarBotao('*', styles.operador)}
      </View>

      <View style={styles.linha}>
        {criarBotao('1')}
        {criarBotao('2')}
        {criarBotao('3')}
        {criarBotao('-', styles.operador)}
      </View>

      <View style={styles.linha}>
        {criarBotao('0', { flex: 2 })}
        {criarBotao('.', styles.botao)}
        {criarBotao('+', styles.operador)}
      </View>

      <View style={styles.linha}>
        <TouchableOpacity style={[styles.botao, styles.limpar]} onPress={limpar}>
          <Text style={styles.textoBotao}>C</Text>
        </TouchableOpacity>
        <TouchableOpacity style={[styles.botao, styles.igual]} onPress={calcularResultado}>
          <Text style={styles.textoBotao}>=</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#1c1c1c',
    justifyContent: 'flex-end',
    padding: 20,
  },
  resultado: {
    fontSize: 60,
    color: '#fff',
    textAlign: 'right',
    marginBottom: 10,
    borderBottomWidth: 1,
    borderColor: '#444',
    paddingBottom: 10,
  },
  linha: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 10,
  },
  botao: {
    backgroundColor: '#333',
    paddingVertical: 20,
    paddingHorizontal: 30,
    borderRadius: 40,
    alignItems: 'center',
    justifyContent: 'center',
    flex: 1,
    marginHorizontal: 5,
  },
  operador: {
    backgroundColor: '#fe9500',
  },
  limpar: {
    backgroundColor: '#ff3b30',
    flex: 1,
    marginRight: 5,
  },
  igual: {
    backgroundColor: '#34c759',
    flex: 1,
    marginLeft: 5,
  },
  textoBotao: {
    fontSize: 28,
    color: '#fff',
  },
});
