import { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';

const TelaProdutos = ({ navigation }) => {
  const [produtosNoCarrinho, setProdutosNoCarrinho] = useState([]);

  const produtos = [
    { id: 1, nome: 'Camiseta', preco: 50 },
    { id: 2, nome: 'Calça', preco: 100 },
    { id: 3, nome: 'Tênis', preco: 150 },
  ];

  const adicionarAoCarrinho = (produto) => {
    setProdutosNoCarrinho([...produtosNoCarrinho, produto]);
  };

  return (
    <View style={{ padding: 20 }}>
      <Text style={{ fontSize: 20 }}>Lista de Produtos</Text>
      {produtos.map((produto) => (
        <View key={produto.id} style={{ marginBottom: 10 }}>
          <Text>{produto.nome} - R${produto.preco}</Text>
          <TouchableOpacity
            style={styles.botaoAdicionar}
            onPress={() => adicionarAoCarrinho(produto)}
          >
            <Text style={styles.textoBotao}>Adicionar ao Carrinho</Text>
          </TouchableOpacity>
        </View>
      ))}
      <TouchableOpacity
        style={styles.botaoVerCarrinho}
        onPress={() => navigation.navigate('Carrinho', { produtosNoCarrinho })}
      >
        <Text style={styles.textoBotao}>Ver Carrinho</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  botaoAdicionar: {
    backgroundColor: '#007BFF',
    padding: 10,
    borderRadius: 5,
    alignItems: 'center',
    marginTop: 5,
  },
  botaoVerCarrinho: {
    backgroundColor: '#FF6347', // Cor de fundo personalizada
    padding: 15,
    borderRadius: 8,
    alignItems: 'center',
    marginTop: 20,
  },
  textoBotao: {
    color: '#FFF', // Cor do texto do botão
    fontWeight: 'bold',
  },
});

export default TelaProdutos;
