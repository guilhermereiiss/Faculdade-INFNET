import { useState } from 'react';
import { View, Text, Button } from 'react-native';
import Categoria from './Categoria.jsx';
import Tarefas from './Tarefas.jsx';

export default function App() {
  const [categorias] = useState(['Mercado', 'Farmácia', 'Estudos']);
  const [tarefas, setTarefas] = useState({});
  const [categoriaSelecionada, setCategoriaSelecionada] = useState(null);

  const adicionarTarefa = (categoria, tarefa) => {
    setTarefas({
      ...tarefas,
      [categoria]: [...(tarefas[categoria] || []), tarefa]
    });
  };

  const removerTarefa = (categoria, index) => {
    setTarefas({
      ...tarefas,
      [categoria]: tarefas[categoria].filter((_, i) => i !== index)
    });
  };

  return (
    <View style={{ flex: 1, padding: 20 }}>
      {categoriaSelecionada ? (
        <Tarefas
          categoria={categoriaSelecionada}
          tarefas={tarefas[categoriaSelecionada] || []}
          adicionarTarefa={adicionarTarefa}
          removerTarefa={removerTarefa}
          voltar={() => setCategoriaSelecionada(null)}
        />
      ) : (
        <Categoria categorias={categorias} selecionarCategoria={setCategoriaSelecionada} />
      )}
    </View>
  );
}
