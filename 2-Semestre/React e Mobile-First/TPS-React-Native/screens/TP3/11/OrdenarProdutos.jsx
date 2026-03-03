
import { View, Picker, StyleSheet } from 'react-native';

export default function OrdenarProdutos({ setCriterioOrdenacao }) {
  return (
    <View style={styles.pickerContainer}>
      <Picker
        selectedValue={'nome-asc'}
        onValueChange={(itemValue) => setCriterioOrdenacao(itemValue)}
      >
        <Picker.Item label="Nome Crescente" value="nome-asc" />
        <Picker.Item label="Nome Decrescente" value="nome-desc" />
        <Picker.Item label="Preço Crescente" value="preco-asc" />
        <Picker.Item label="Preço Decrescente" value="preco-desc" />
      </Picker>
    </View>
  );
}

const styles = StyleSheet.create({
  pickerContainer: {
    margin: 10,
  },
});
