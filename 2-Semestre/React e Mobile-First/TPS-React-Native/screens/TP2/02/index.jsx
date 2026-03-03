
import { SafeAreaView, StyleSheet } from 'react-native';
import ImageCarousel from './ImagemCarrosel.jsx';

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <ImageCarousel />
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
