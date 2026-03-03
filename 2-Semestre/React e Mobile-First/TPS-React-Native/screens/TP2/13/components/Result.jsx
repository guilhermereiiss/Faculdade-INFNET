import React from 'react';
import { View, Text } from 'react-native';
import styles from '../styles.jsx';

function Result({ score, total }) {
  return (
    <View style={styles.optionsButton}>
      <Text>Quiz Terminado!</Text>
      <Text>Sua pontuação foi: {score} de {total}</Text>
    </View>
  );
}

export default Result;
