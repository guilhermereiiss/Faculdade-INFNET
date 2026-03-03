
import { View, Text, StyleSheet } from 'react-native';

export default function TransacaoItemList({ transacao }) {
  return (
    <View style={styles.card}>
      <Text style={styles.descricao}>{transacao.descricao}</Text>
      <Text style={styles.valor}>{transacao.valor}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  card: { 
    padding: 16, 
    marginBottom: 16, 
    borderWidth: 1, 
    borderRadius: 8 
  },
  descricao: { 
    fontSize: 16, 
    marginBottom: 8 
  },
  valor: { 
    fontSize: 16, 
    fontWeight: 'bold' },
});
