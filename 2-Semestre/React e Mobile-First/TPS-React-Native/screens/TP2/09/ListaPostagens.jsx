
import { View, Text, FlatList, TouchableOpacity, StyleSheet } from 'react-native';

const dadosPostagens = [
    { id: '1', titulo: 'Postagem 1', resumo: 'Resumo da postagem 1' },
    { id: '2', titulo: 'Postagem 2', resumo: 'Resumo da postagem 2' },
    { id: '3', titulo: 'Postagem 3', resumo: 'Resumo da postagem 3' },
];

export default function ListaPostagens({ navigation }) {
    return (
        <FlatList
            data={dadosPostagens}
            keyExtractor={(item) => item.id}
            renderItem={({ item }) => (
                <TouchableOpacity
                    style={estilos.itemContainer}
                    onPress={() => navigation.navigate('DetalhesPostagem')}
                >
                    <Text style={estilos.titulo}>{item.titulo}</Text>
                    <Text style={estilos.resumo}>{item.resumo}</Text>
                </TouchableOpacity>
            )}
        />
    );
}

const estilos = StyleSheet.create({
    itemContainer: {
        padding: 15,
        margin: 10,
        borderWidth: 1,
        borderColor: '#ddd',
        borderRadius: 5,
    },
    titulo: {
        fontSize: 18,
        fontWeight: 'bold',
    },
    resumo: {
        fontSize: 14,
        color: '#666',
    },
});
