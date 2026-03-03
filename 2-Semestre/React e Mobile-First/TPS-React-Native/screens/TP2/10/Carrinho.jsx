
import { View, Text, Button } from 'react-native';

const TelaCarrinho = ({ route, navigation }) => {
  const { produtosNoCarrinho } = route.params;

  return (
    <View style={{ padding: 20 }}>
      <Text style={{ fontSize: 20 }}>Carrinho de Compras</Text>
      {produtosNoCarrinho.length === 0 ? (
        <Text>O carrinho está vazio.</Text>
      ) : (
        produtosNoCarrinho.map((produto, index) => (
          <View key={index} style={{ marginBottom: 10 }}>
            <Text>{produto.nome} - R${produto.preco}</Text>
          </View>
        ))
      )}
    </View>
  );
};

export default TelaCarrinho;
