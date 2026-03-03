import { useState, useEffect } from 'react';
import { View, Text, StyleSheet, Picker, FlatList, Alert, TouchableOpacity, Dimensions } from 'react-native';
import { listarMoedas, obterCotacao } from '../api/cotacaoAPI.jsx';
import BotaoAdicionar from '../components/Button/BotaoAdicionar.jsx';
import ModalTransacao from './ModalNovaTransacao.jsx';
import { Swipeable } from 'react-native-gesture-handler';

export default function TransacaoListScreen() {
  const [transacoes, setTransacoes] = useState([
    { id: 1, descricao: 'Compra na Pichau', moeda: 'BRL', tipo: 'Despesa', valor: 15000.0, categoria: 'Lazer', data: '2024-12-06T10:00:00Z' },
    { id: 2, descricao: 'Carro', moeda: 'USD', tipo: 'Receita', valor: 89000.0, categoria: 'Venda', data: '2024-12-05T14:00:00Z' },
    { id: 3, descricao: 'Pagamento de aluguel', moeda: 'BRL', tipo: 'Despesa', valor: 900.0, categoria: 'Custos', data: '2024-12-04T16:00:00Z' },
  ]);
  const [categorias, setCategorias] = useState(['Lazer', 'Venda', 'Custos']);
  const [moedasDisponiveis, setMoedasDisponiveis] = useState([]);
  const [modalVisivel, setModalVisivel] = useState(false);
  const [transacaoEditando, setTransacaoEditando] = useState(null);
  const [filtro, setFiltro] = useState('');
  const [ordenacao, setOrdenacao] = useState('');
  const [isPortrait, setIsPortrait] = useState(true);

  useEffect(() => {
    const updateLayout = () => {
      const { width, height } = Dimensions.get('window');
      setIsPortrait(height >= width);
    };

    Dimensions.addEventListener('change', updateLayout);
    return () => {
      Dimensions.removeEventListener('change', updateLayout);
    };
  }, []);

  useEffect(() => {
    async function carregarMoedas() {
      const moedas = await listarMoedas();
      setMoedasDisponiveis(moedas.map((moeda) => moeda.simbolo));
    }
    carregarMoedas();
  }, []);

  const adicionarCategoria = (novaCategoria) => {
    if (!categorias.includes(novaCategoria)) {
      setCategorias([...categorias, novaCategoria]);
    }
  };

  const adicionarTransacao = async (novaTransacao) => {
    const { moeda, valor } = novaTransacao;
    if (moeda !== 'BRL') {
      const dataAtual = new Date().toISOString().split('T')[0].split('-').reverse().join('-');
      const cotacao = await obterCotacao(moeda, dataAtual);
      if (!cotacao) {
        Alert.alert('Erro', `Não foi possível obter a cotação para a moeda ${moeda}.`);
        return;
      }
      novaTransacao.valor *= cotacao.cotacaoVenda;
    }
    if (transacaoEditando) {
      setTransacoes(transacoes.map((t) => (t.id === transacaoEditando.id ? novaTransacao : t)));
    } else {
      setTransacoes([...transacoes, novaTransacao]);
    }
    setModalVisivel(false);
    setTransacaoEditando(null);
  };

  const editarTransacao = (id) => {
    const transacaoParaEditar = transacoes.find((transacao) => transacao.id === id);
    if (transacaoParaEditar) {
      setTransacaoEditando(transacaoParaEditar);
      setModalVisivel(true);
    }
  };

  const deletarTransacao = (id) => {
    setTransacoes(transacoes.filter((transacao) => transacao.id !== id));
  };

  const renderItem = ({ item }) => (
    <Swipeable
      renderLeftActions={() => (
        <TouchableOpacity style={styles.botaoEditar} onPress={() => editarTransacao(item.id)}>
          <Text style={styles.textoBotao}>Editar</Text>
        </TouchableOpacity>
      )}
      renderRightActions={() => (
        <TouchableOpacity style={styles.botaoExcluir} onPress={() => deletarTransacao(item.id)}>
          <Text style={styles.textoBotao}>Apagar</Text>
        </TouchableOpacity>
      )}
    >
      <View style={styles.card}>
        <Text style={styles.cardDescricao}>{item.descricao}</Text>
        {isPortrait ? (
          <>
            <Text style={styles.cardInfo}>Categoria: {item.categoria}</Text>
            <Text style={styles.cardInfoValor}>Valor: R$ {item.valor.toFixed(2)}</Text>
            <Text style={styles.cardInfo}>Data: {new Date(item.data).toLocaleDateString()}</Text>
          </>
        ) : (
          <>
            <Text style={styles.cardInfo}>Categoria: {item.categoria}</Text>
            <Text style={styles.cardInfo}>Moeda: {item.moeda}</Text>
            <Text style={styles.cardInfo}>Tipo: {item.tipo}</Text>
            <Text style={styles.cardInfo}>Hora: {new Date(item.data).toLocaleTimeString()}</Text>
            <Text style={styles.cardValor}>R$ {item.valor.toFixed(2)}</Text>
          </>
        )}
      </View>
    </Swipeable>
  );

  const transacoesFiltradas = filtro ? transacoes.filter((transacao) => transacao.categoria === filtro) : transacoes;
  const transacoesOrdenadas = ordenacao === 'Valor' ? transacoesFiltradas.sort((a, b) => a.valor - b.valor) : transacoesFiltradas;

  return (
    <View style={styles.container}>
      <View style={styles.filtros}>
        <Picker style={styles.picker} selectedValue={filtro} onValueChange={(itemValue) => setFiltro(itemValue)}>
          <Picker.Item label="Filtrar por Categoria" value="" />
          {categorias.map((categoria) => (
            <Picker.Item key={categoria} label={categoria} value={categoria} />
          ))}
        </Picker>
        <Picker style={styles.picker} selectedValue={ordenacao} onValueChange={(itemValue) => setOrdenacao(itemValue)}>
          <Picker.Item label="Ordenar por" value="" />
          <Picker.Item label="Descrição" value="Descrição" />
          <Picker.Item label="Valor" value="Valor" />
        </Picker>
      </View>
      <FlatList
        data={transacoesOrdenadas}
        renderItem={renderItem}
        keyExtractor={(item) => item.id.toString()}
        contentContainerStyle={styles.scrollViewContent}
        style={styles.flatList}
      />
      <View style={styles.footer}>
        <BotaoAdicionar onPress={() => setModalVisivel(true)} />
      </View>
      <ModalTransacao
        visivel={modalVisivel}
        fecharModal={() => setModalVisivel(false)}
        adicionarTransacao={adicionarTransacao}
        adicionarCategoria={adicionarCategoria}
        moedasDisponiveis={moedasDisponiveis}
        transacaoEditando={transacaoEditando}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#0E1826' },  
  filtros: { 
    flexDirection: 'row', 
    padding: 15, 
    backgroundColor: '#1C2534',  
    borderBottomWidth: 1, 
    borderBottomColor: '#3C4753'  
  },
  picker: { 
    flex: 1, 
    height: 45, 
    borderColor: '#3C4753', 
    borderWidth: 1, 
    borderRadius: 8, 
    marginRight: 10, 
    backgroundColor: '#2A3542',
    color: '#ffff'
  },
  flatList: { flex: 1 },
  scrollViewContent: { paddingBottom: 60 },
  card: { 
    padding: 20, 
    margin: 12, 
    backgroundColor: '#1C2534',  
    borderRadius: 10, 
    shadowColor: '#000', 
    shadowOpacity: 0.1, 
    shadowRadius: 5, 
    elevation: 5 
  },
  cardDescricao: { 
    fontSize: 18, 
    fontWeight: 'bold', 
    color: '#ffffff'  
  },
  cardInfo: { 
    fontSize: 14, 
    color: '#B0BEC5', 
    marginVertical: 4 
  },
  cardInfoValor: { 
    fontSize: 14, 
    color: '#81C784', 
    marginVertical: 4 
  },
  cardValor: { 
    fontSize: 16, 
    color: '#81C784',  
    fontWeight: 'bold', 
    marginTop: 10 
  },
  swipeActions: { 
    flexDirection: 'row', 
    alignItems: 'center' 
  },
  botaoExcluir: { 
    backgroundColor: '#FF5252',  
    padding: 15, 
    justifyContent: 'center', 
    alignItems: 'center' 
  },
  botaoEditar: { 
    backgroundColor: '#42A5F5',  
    padding: 15, 
    justifyContent: 'center', 
    alignItems: 'center' 
  },
  textoBotao: { 
    color: '#ffffff', 
    fontSize: 16 
  },
  footer: { 
    padding: 20, 
    justifyContent: 'center', 
    alignItems: 'center' 
  },
});
