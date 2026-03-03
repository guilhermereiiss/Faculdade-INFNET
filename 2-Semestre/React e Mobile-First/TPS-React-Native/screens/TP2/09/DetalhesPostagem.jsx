
import { View, Text, StyleSheet } from 'react-native';

export default function DetalhesPostagem() {
    return (
        <View style={estilos.container}>
            <Text style={estilos.titulo}>Detalhes da Postagem</Text>
            <Text style={estilos.textoCompleto}>
                Este é o conteúdo completo da postagem. Sem parâmetros sendo passados entre as telas.
            </Text>
            <Text style={estilos.autor}>Autor: Nome do Autor</Text>
            <Text style={estilos.data}>Postado em: 01/01/2024 10:00</Text>
        </View>
    );
}

const estilos = StyleSheet.create({
    container: {
        flex: 1,
        padding: 20,
    },
    titulo: {
        fontSize: 24,
        fontWeight: 'bold',
        marginBottom: 10,
    },
    textoCompleto: {
        fontSize: 16,
        color: '#333',
        marginVertical: 15,
    },
    autor: {
        fontSize: 14,
        color: '#666',
        marginTop: 20,
    },
    data: {
        fontSize: 14,
        color: '#666',
    },
});
