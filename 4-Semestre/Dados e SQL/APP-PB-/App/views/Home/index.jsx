import { Text, View, StyleSheet } from 'react-native';

const HomeScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Match Movie</Text>
      <Text>Seja bem-vindo, o melhor App de filmes</Text>
    </View>
  )
}

export default HomeScreen

const cores = {
  corPrimaria: '#ffffff',
  corSecundaria: '#281259',
  corTerciaria: '#000000',
  corBotao: '#9F2CBF',
  corBotaoTexto: '#000000',
  corCard: '#281259',
  corCardTexto: '#ffffff',
  sombraCard: 'rgba(0, 0, 0, 0.1)',
  sombraHover: 'rgba(0, 0, 0, 0.2)',
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: cores.corPrimaria,  
    alignItems: 'center',
    justifyContent: 'center',
  },
  text: {
    color: cores.corSecundaria,  
    fontSize: 24,
    fontWeight: 'bold',
  },
});
