
import { View, Text } from 'react-native';

export default function DetalhesPostagem({ route }) {
  const { viagem } = route.params;

  return (
    <View style={{ flex: 1, padding: 20 }}>
      <Text style={{ fontSize: 24 }}>{viagem.destino}</Text>
      <Text>{`Início: ${viagem.inicio} - Fim: ${viagem.fim}`}</Text>
      <Text>{`Nota: ${viagem.nota}/5`}</Text>
      <Text style={{ marginTop: 20 }}>Detalhes completos da viagem...</Text>
    </View>
  );
}
