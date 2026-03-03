
import { View, Text, FlatList } from 'react-native';

const amigos = [
  { id: '1', nome: 'João' },
  { id: '2', nome: 'Maria' },
];

export default function Amigos() {
  return (
    <View style={{ flex: 1 }}>
      <FlatList
        data={amigos}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View style={{ padding: 15, borderBottomWidth: 1, borderBottomColor: '#ccc' }}>
            <Text>{item.nome}</Text>
          </View>
        )}
      />
    </View>
  );
}
