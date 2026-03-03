import{ useState } from 'react';
import { View, Text, Button, FlatList } from 'react-native';
import InputTarefa from './InputTarefa.jsx';

export default function Tarefas({ categoria, tarefas, adicionarTarefa, removerTarefa, voltar }) {
  const [novaTarefa, setNovaTarefa] = useState('');

  return (
    <View>
      <Text style={{ fontSize: 24, marginBottom: 10 }}>{categoria}</Text>
      <InputTarefa
        valor={novaTarefa}
        onChange={setNovaTarefa}
        onAdicionar={() => {
          adicionarTarefa(categoria, novaTarefa);
          setNovaTarefa('');
        }}
      />
      <FlatList
        data={tarefas}
        renderItem={({ item, index }) => (
          <View style={{ flexDirection: 'row', alignItems: 'center', marginVertical: 5 }}>
            <Text style={{ flex: 1 }}>{item}</Text>
            <Button title="Remover" onPress={() => removerTarefa(categoria, index)} />
          </View>
        )}
        keyExtractor={(item, index) => index.toString()}
      />
      <Button title="Voltar" onPress={voltar} />
    </View>
  );
}
