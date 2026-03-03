import { useState } from 'react';
import { Text, View, TouchableOpacity, StyleSheet } from 'react-native';

export default function App() {
  const [count, setCount] = useState(0);

  return (
    <View style={styles.container}>
      <TouchableOpacity onPress={() => setCount(count - 1)}>
        <Text style={styles.operator}>-</Text>
      </TouchableOpacity>

      <Text style={styles.counter}>{count}</Text>

      <TouchableOpacity onPress={() => setCount(count + 1)}>
        <Text style={styles.operator}>+</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    flex: 1,
  },
  counter: {
    fontSize: 40,
    marginHorizontal: 20,
  },
  operator: {
    fontSize: 40,
    padding: 10,
  },
});
