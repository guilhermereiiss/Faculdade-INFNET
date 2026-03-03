
import { View, StyleSheet } from 'react-native';
import ListaEsp from './ListaEspaço.jsx';

export default function App() {
  
  const data = [
    { id: 1, name: '1' },
    { id: 2, name: '2' },
    { id: 3, name: '3' },
    { id: 4, name: '4' },
  ];

  return (
    <View style={styles.container}>
      <ListaEsp data={data} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f0f4f8',
    paddingTop: 50,
  },
});
