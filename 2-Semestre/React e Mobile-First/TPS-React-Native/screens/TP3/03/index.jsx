
import { View, StyleSheet } from 'react-native';
import Lista from './Lista.jsx';

export default function App() {
  const tarefas = [
    { id: 1, nome: 'Comprar pão' },
    { id: 2, nome: 'Fazer exercícios' },
    { id: 3, nome: 'Estudar React Native' },
    { id: 4, nome: 'Ler um livro' },
    { id: 5, nome: 'Organizar a casa' },
  ];

  return (
    <View style={styles.container}>
      <Lista itens={tarefas} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f4f4f4',
    padding: 20,
  },
});
