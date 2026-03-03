import { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, FlatList, StyleSheet, Alert } from 'react-native';

export default function App() {
    const [tarefa, setTarefa] = useState('');
    const [listaTarefas, setListaTarefas] = useState([]);

    const adicionarTarefa = () => {
        if (tarefa.trim() === '') {
            Alert.alert('Erro', 'A tarefa não pode estar vazia!');
            return;
        }
        setListaTarefas([...listaTarefas, { id: Date.now(), nome: tarefa }]);
        setTarefa('');
    };

    const removerTarefa = (id) => {
        setListaTarefas(listaTarefas.filter((item) => item.id !== id));
    };

    const renderizarItem = ({ item }) => (
        <View style={styles.tarefaContainer}>
            <Text style={styles.textoTarefa}>{item.nome}</Text>
            <TouchableOpacity onPress={() => removerTarefa(item.id)}>
                <Text style={styles.botaoRemover}>Remover</Text>
            </TouchableOpacity>
        </View>
    );

    return (
        <View style={styles.container}>
            <Text style={styles.titulo}>Lista de Tarefas</Text>
            <TextInput
                style={styles.input}
                placeholder="Digite uma tarefa"
                value={tarefa}
                onChangeText={setTarefa}
            />
            <TouchableOpacity style={styles.botao} onPress={adicionarTarefa}>
                <Text style={styles.textoBotao}>Adicionar</Text>
            </TouchableOpacity>
            <FlatList
                data={listaTarefas}
                keyExtractor={(item) => item.id.toString()}
                renderItem={renderizarItem}
                style={styles.lista}
            />
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#f5f5f5',
        padding: 20,
        justifyContent: 'center',
    },
    titulo: {
        fontSize: 24,
        fontWeight: 'bold',
        marginBottom: 20,
        textAlign: 'center',
    },
    input: {
        borderWidth: 1,
        borderColor: '#ddd',
        borderRadius: 8,
        padding: 10,
        marginBottom: 10,
        backgroundColor: '#fff',
    },
    botao: {
        backgroundColor: '#6200ee',
        padding: 15,
        borderRadius: 8,
        alignItems: 'center',
        marginBottom: 20,
    },
    textoBotao: {
        color: '#fff',
        fontSize: 18,
    },
    lista: {
        marginTop: 10,
    },
    tarefaContainer: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        padding: 15,
        borderBottomWidth: 1,
        borderColor: '#ddd',
        backgroundColor: '#fff',
        marginBottom: 5,
        borderRadius: 8,
    },
    textoTarefa: {
        fontSize: 16,
    },
    botaoRemover: {
        color: '#ff3b30',
        fontWeight: 'bold',
    },
});
