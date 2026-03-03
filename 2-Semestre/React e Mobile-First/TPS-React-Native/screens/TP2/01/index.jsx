import { SafeAreaView, StyleSheet } from 'react-native';
import TaskList from './TaskList';

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <TaskList />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f8f9fa',
    paddingTop: 50,
  },
});
