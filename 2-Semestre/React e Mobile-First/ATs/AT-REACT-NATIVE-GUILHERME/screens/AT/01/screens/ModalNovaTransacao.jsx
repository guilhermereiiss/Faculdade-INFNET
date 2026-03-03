import { useState, useEffect } from 'react';
import { Modal, View, TextInput, Button, StyleSheet, Picker, TouchableOpacity, Text, Platform, Switch, } from 'react-native';
import DateTimePicker from '@react-native-community/datetimepicker';
import { listarMoedas, obterCotacao } from '../api/cotacaoAPI.jsx';

export default function ModalTransacao({
  visivel,
  fecharModal,
  adicionarTransacao,
  adicionarCategoria,
}) {
  const [descricao, setDescricao] = useState('');
  const [valor, setValor] = useState('');
  const [moeda, setMoeda] = useState('BRL');
  const [tipo, setTipo] = useState('Receita');
  const [categoria, setCategoria] = useState('');
  const [dataHora, setDataHora] = useState(new Date());
  const [mostrarDateTimePicker, setMostrarDateTimePicker] = useState(false);
  const [moedas, setMoedas] = useState([]);
  const [cotacao, setCotacao] = useState(null);

  useEffect(() => {
    const carregarMoedas = async () => {
      const moedasListadas = await listarMoedas();
      setMoedas(moedasListadas);
    };
    carregarMoedas();
  }, []);

  const salvarTransacao = () => {
    adicionarTransacao({
      id: Date.now(),
      descricao,
      valor: parseFloat(valor),
      moeda,
      tipo,
      categoria,
      dataHora,
    });
    if (adicionarCategoria && categoria) {
      adicionarCategoria(categoria);
    }
    setDescricao('');
    setValor('');
    setTipo('Receita');
    setCategoria('');
    setDataHora(new Date());
    setCotacao(null);
  };

  const exibirDateTimePicker = () => {
    setMostrarDateTimePicker(true);
  };

  const ocultarDateTimePicker = () => {
    setMostrarDateTimePicker(false);
  };

  const aoAlterarDataHora = (_, selecionado) => {
    if (selecionado) {
      setDataHora(selecionado);
      ocultarDateTimePicker();
    }
  };

  const buscarCotacao = async () => {
    const dataFormatada = dataHora.toISOString().split('T')[0].split('-').reverse().join('-');
    const resultadoCotacao = await obterCotacao(moeda, dataFormatada);
    setCotacao(resultadoCotacao ? resultadoCotacao.cotacaoCompra : 'Cotação indisponível no momento');
  };

  return (
    <Modal visible={visivel} animationType="slide" transparent={true}>
      <View style={styles.modalContainer}>
        <View style={styles.modalContent}>
          <TextInput
            style={styles.input}
            placeholder="Descrição"
            value={descricao}
            onChangeText={setDescricao}
          />
          <TextInput
            style={styles.input}
            placeholder="Valor"
            value={valor}
            onChangeText={setValor}
            keyboardType="numeric"
          />
          <TextInput
            style={styles.input}
            placeholder="Categoria"
            value={categoria}
            onChangeText={setCategoria}
          />
          <TouchableOpacity onPress={exibirDateTimePicker} style={styles.dataHoraBotao}>
            <Text style={styles.dataHoraTexto}>
              {dataHora.toLocaleDateString()} {dataHora.toLocaleTimeString()}
            </Text>
          </TouchableOpacity>
          {mostrarDateTimePicker && (
            <DateTimePicker
              value={dataHora}
              mode="datetime"
              display={Platform.OS === 'ios' ? 'spinner' : 'default'}
              onChange={aoAlterarDataHora}
            />
          )}
          <Picker selectedValue={moeda} style={styles.picker} onValueChange={setMoeda}>
            {moedas.map((item) => (
              <Picker.Item key={item.simbolo} label={item.nomeFormatado} value={item.simbolo} />
            ))}
          </Picker>
          <Button title="Buscar sobre a Cotação" onPress={buscarCotacao} />
          {cotacao && <Text style={styles.cotacaoTexto}>Cotação: {cotacao}</Text>}
          <View style={styles.switchContainer}>
            <Text style={styles.switchLabel}>{tipo === 'Receita' ? 'Receita' : 'Despesa'}</Text>
            <Switch
              value={tipo === 'Receita'}
              onValueChange={() => setTipo((prev) => (prev === 'Receita' ? 'Despesa' : 'Receita'))}
              trackColor={{ false: '#ccc', true: '#007BFF' }}
              thumbColor={Platform.OS === 'android' ? '#fff' : undefined}
            />
          </View>
          <Button title="Salvar" onPress={salvarTransacao} color="#45b1f5" />
          <Button title="Cancelar" onPress={fecharModal} color="red" />
        </View>
      </View>
    </Modal>
  );
}


const styles = StyleSheet.create({
  modalContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'rgba(0, 0, 0, 0.5)'
  },
  modalContent: {
    width: '90%',
    padding: 20,
    backgroundColor: '#1C2534',
    borderRadius: 15,
    elevation: 5
  },
  input: {
    height: 50,
    borderColor: '#3C4753',
    borderWidth: 1,
    borderRadius: 10,
    marginBottom: 15,
    paddingLeft: 15,
    fontSize: 16,
    color: '#ffffff'
  },
  dataHoraBotao: {
    height: 50,
    backgroundColor: '#42A5F5',
    borderRadius: 10,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 15
  },
  dataHoraTexto: {
    color: 'white',
    fontSize: 16
  },
  picker: {
    height: 50,
    borderColor: '#3C4753',
    borderWidth: 1,
    borderRadius: 10,
    marginBottom: 15,
    color: 'black'
  },
  cotacaoTexto: {
    fontSize: 16,
    color: '#81C784',
    marginBottom: 15
  },
  switchContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 15
  },
  switchLabel: {
    fontSize: 16,
    marginRight: 10,
    color: '#ffffff'
  },
});
