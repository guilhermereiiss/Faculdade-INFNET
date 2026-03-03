
import { View, Text, Button, StyleSheet } from 'react-native';
import { useNavigation } from '@react-navigation/native';

const Questao = ({ pergunta, opcoes, onProximo, proximaTela }) => {
  const navigation = useNavigation();

  return (
    <View style={styles.container}>
      <Text style={styles.pergunta}>{pergunta}</Text>
      {opcoes.map((opcao, index) => (
        <Button key={index} title={opcao} onPress={() => {}} />
      ))}
      <Button
        title="Próxima"
        onPress={() => {
          onProximo();
          navigation.navigate(proximaTela);
        }}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  pergunta: {
    fontSize: 18,
    marginBottom: 20,
  },
});

export default Questao;
