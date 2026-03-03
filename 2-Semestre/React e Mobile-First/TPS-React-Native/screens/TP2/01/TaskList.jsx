
import { View, StyleSheet, FlatList } from 'react-native';
import TaskItem from './TaskItem';

const tasks = [
  { id: '1', title: 'Comprar mantimentos' },
  { id: '2', title: 'Ir à academia' },
  { id: '3', title: 'Estudar React Native' },
  { id: '4', title: 'Ler um livro' },
];

export default function TaskList() {
  return (
    <View style={styles.listContainer}>
      <FlatList
        data={tasks}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => <TaskItem title={item.title} />}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  listContainer: {
    flex: 1,
    width: '100%',
    paddingHorizontal: 20,
    marginTop: 10,
  },
});
