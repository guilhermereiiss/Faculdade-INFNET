import React, { useState } from 'react';
import { Text, View, Pressable, StyleSheet } from 'react-native';

export default function App() {
  const [count, setCount] = useState(0);

  return (
    <View style={styles.container}>
      <Pressable
        onPress={() => setCount(count - 1)}
        underlayColor="#DDDDDD"
        style={styles.button}
      >
        <Text style={styles.operator}>-</Text>
      </Pressable>

      <Text style={styles.counter}>{count}</Text>

      <Pressable
        onPress={() => setCount(count + 1)}
        underlayColor="#DDDDDD"
        style={styles.button}
      >
        <Text style={styles.operator}>+</Text>
      </Pressable>
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
  },
  button: {
    padding: 10,
    borderRadius: 5,
  },
});
