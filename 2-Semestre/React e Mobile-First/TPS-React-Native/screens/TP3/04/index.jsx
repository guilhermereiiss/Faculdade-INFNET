import { View, StyleSheet } from 'react-native';
import Lista from './Lista.jsx';

export default function App() {
  const atividadesPorCategoria = [
    {
      title: 'Manhã',
      data: ['Ir pra academia', 'Preparar café da manhã', 'Organizar agenda'],
    },
    {
      title: 'Tarde',
      data: ['Almoçar', 'Estudar React Native', 'Fazer TP'],
    },
    {
      title: 'Noite',
      data: ['Jantar em família', 'Ler um mangá do One Piece', 'Relaxar assistindo Dexter'],
    },
  ];

  return (
    <View style={styles.container}>
      <Lista categorias={atividadesPorCategoria} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'flex-start',
    alignItems: 'stretch',
    backgroundColor: '#e3f2fd',
  },
});
