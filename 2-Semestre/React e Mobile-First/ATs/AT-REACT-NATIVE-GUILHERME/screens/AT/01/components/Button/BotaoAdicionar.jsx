
import { TouchableOpacity, StyleSheet } from 'react-native';
import { Ionicons } from '@expo/vector-icons';

export default function BotaoAdicionar({ onPress }) {
  return (
    <TouchableOpacity style={styles.botao} onPress={onPress}>
      <Ionicons name="add" size={24} color="white" />
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  botao: {
    position: 'absolute',
    bottom: 20,
    right: 20,
    backgroundColor: '#F29F05',
    width: 60,
    height: 60,
    borderRadius: 30,
    justifyContent: 'center',
    alignItems: 'center',
    elevation: 4,
  },
});
