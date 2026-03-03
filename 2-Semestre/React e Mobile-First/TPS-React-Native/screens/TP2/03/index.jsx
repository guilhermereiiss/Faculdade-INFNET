import React from 'react';
import { SafeAreaView, StyleSheet } from 'react-native';
import ImageGrid from './ImageGrid.jsx';

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <ImageGrid />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f8f9fa',
  },
});
