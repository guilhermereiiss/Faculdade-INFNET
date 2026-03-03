
import { View, TextInput, Button } from 'react-native';

export default function InputTarefa({ valor, onChange, onAdicionar }) {
  return (
    <View style={{ flexDirection: 'row', marginBottom: 10 }}>
      <TextInput
        style={{ flex: 1, borderColor: 'gray', borderWidth: 1, marginRight: 10, padding: 5 }}
        value={valor}
        onChangeText={onChange}
        placeholder="Nova Tarefa"
      />
      <Button title="Adicionar" onPress={onAdicionar} />
    </View>
  );
}
