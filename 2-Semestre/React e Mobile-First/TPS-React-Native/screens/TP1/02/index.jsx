import { View, Text, StyleSheet } from 'react-native';

const obterHoraAtual = () => {
    const data = new Date();
    return data.toLocaleTimeString();
};

export default function App() {
    const nomeCompleto = "Guilherme Reis de Jesus Santos";
    const horaAtual = obterHoraAtual();

    return (
        <View style={styles.container}>
            <Text style={styles.texto}>
                Olá, {nomeCompleto}! Agora são {horaAtual}.
            </Text>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#f0f0f0',
    },
    texto: {
        fontSize: 24,
        fontWeight: 'bold',
        textAlign: 'center',
    },
});
