
import { View, Text, StyleSheet } from 'react-native';

export default function TaskItem({ title }) {
  return (
    <View style={styles.itemContainer}>
      <Text style={styles.itemText}>{title}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  itemContainer: {
    backgroundColor: '#e1e5ea',
    padding: 15,
    marginVertical: 8,
    borderRadius: 8,
    alignItems: 'center',
  },
  itemText: {
    fontSize: 16,
    color: '#333',
  },
});
