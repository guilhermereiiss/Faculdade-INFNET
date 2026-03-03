
import { View, StyleSheet } from 'react-native';
import ListaContatos from './ListaContatos.jsx';

export default function App() {
  const dadosContatos = [
    {
      id: 1,
      avatar: 'https://i.pravatar.cc/400?img=64',
      nome: 'Antonio Gustavo',
      endereco: 'Rua A, 123',
      numero: '(11) 98765-4321',
    },
    {
      id: 2,
      avatar: 'https://i.pravatar.cc/100?img=2',
      nome: 'Maria Oliveira',
      endereco: 'Av. B, 456',
      numero: '(21) 99876-5432',
    },
    {
      id: 3,
      avatar: 'https://i.pravatar.cc/100?img=3',
      nome: 'Carlos Souza',
      endereco: 'Rua C, 789',
      numero: '(31) 91234-5678',
    },
  ];

  return (
    <View style={estilos.container}>
      <ListaContatos dados={dadosContatos} />
    </View>
  );
}

const estilos = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
    paddingTop: 50,
  },
});
