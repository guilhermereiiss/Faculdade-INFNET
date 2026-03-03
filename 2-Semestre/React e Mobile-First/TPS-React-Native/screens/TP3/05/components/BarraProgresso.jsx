
import { View, StyleSheet } from 'react-native';

const BarraProgresso = ({ progresso }) => {
  return (
    <View style={styles.container}>
      <View style={[styles.progresso, { width: `${progresso * 100}%` }]} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    height: 10,
    width: '100%',
    backgroundColor: '#ccc',
    borderRadius: 5,
    overflow: 'hidden',
    marginVertical: 20,
  },
  progresso: {
    height: '100%',
    backgroundColor: '#4caf50',
  },
});

export default BarraProgresso;
