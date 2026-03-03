
import { View, StyleSheet } from 'react-native';
import Direita from './praDireita.jsx';

export default function App() {
 
  const data = [
    { id: 1, name: '1' },
    { id: 2, name: '2' },
    { id: 3, name: '3' },
    { id: 4, name: '4' },
  ];

  return (
    <View style={styles.container}>
      <Direita data={data} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f8f8f8',
    paddingTop: 50,
  },
});
