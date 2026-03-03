
import { View, Text, FlatList } from 'react-native';

const minhasViagens = [
  { id: '1', destino: 'Londres', inicio: '2023-12-01', fim: '2023-12-10', nota: 4 },
];

export default function MinhasViagens() {
  return (
    <View style={{ flex: 1 }}>
      <FlatList
        data={minhasViagens}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View style={{ padding: 15, borderBottomWidth: 1, borderBottomColor: '#ccc' }}>
            <Text style={{ fontSize: 18 }}>{item.destino}</Text>
            <Text>{`Início: ${item.inicio} - Fim: ${item.fim}`}</Text>
            <Text>{`Nota: ${item.nota}/5`}</Text>
          </View>
        )}
      />
    </View>
  );
}
