import  { useState } from 'react';
import { View, Text, Button, FlatList, TouchableOpacity } from 'react-native';

const viagensContatos = [
  { id: '1', destino: 'Paris', inicio: '2024-01-15', fim: '2024-01-20', nota: 5 },
  { id: '2', destino: 'Tokyo', inicio: '2024-03-10', fim: '2024-03-15', nota: 4 },
];

export default function FeedContatos({ navigation }) {
  const [curtidas, setCurtidas] = useState({});

  const curtirPostagem = (id) => {
    setCurtidas({ ...curtidas, [id]: (curtidas[id] || 0) + 1 });
  };

  return (
    <View style={{ flex: 1 }}>
      <FlatList
        data={viagensContatos}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View style={{ padding: 15, borderBottomWidth: 1, borderBottomColor: '#ccc' }}>
            <TouchableOpacity onPress={() => navigation.navigate('DetalhesPostagem', { viagem: item })}>
              <Text style={{ fontSize: 18 }}>{item.destino}</Text>
              <Text>{`Início: ${item.inicio} - Fim: ${item.fim}`}</Text>
              <Text>{`Nota: ${item.nota}/5`}</Text>
            </TouchableOpacity>
            <Button title="Curtir" onPress={() => curtirPostagem(item.id)} />
            <Text>{curtidas[item.id] || 0} curtidas</Text>
          </View>
        )}
      />
    </View>
  );
}
