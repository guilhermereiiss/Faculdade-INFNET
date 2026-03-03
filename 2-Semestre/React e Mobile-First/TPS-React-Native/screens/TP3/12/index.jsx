import { useState, useEffect } from 'react';
import { View, Text, FlatList, ActivityIndicator, StyleSheet } from 'react-native';

const ListaProposicoes = () => {
    const [dados, setDados] = useState([]);
    const [pagina, setPagina] = useState(1);
    const [carregando, setCarregando] = useState(false);


    const carregarDados = async () => {
        if (carregando) return;
        setCarregando(true);
        try {
            const resposta = await fetch(`https://dadosabertos.camara.leg.br/api/v2/proposicoes?pagina=${pagina}&itens=10`);
            const resultado = await resposta.json();
            setDados([...dados, ...resultado.dados]);
            setPagina(pagina + 1);
        } catch (error) {
            console.error(error);
        } finally {
            setCarregando(false);
        }
    };

    useEffect(() => {
        carregarDados();
    }, []);

    const renderItem = ({ item }) => (
        <View style={styles.itemContainer}>
            <Text style={styles.titulo}>{item.ementa || 'Sem título'}</Text>
            <Text style={styles.detalhes}>ID: {item.id}</Text>
        </View>
    );

    return (
        <View style={styles.container}>
            <FlatList
                data={dados}
                keyExtractor={(item, index) => index.toString()}
                renderItem={renderItem}
                onEndReached={carregarDados}
                onEndReachedThreshold={0.5}
                ListFooterComponent={carregando ? <ActivityIndicator size="large" color="#0000ff" /> : null}
            />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 10,
        backgroundColor: '#fff',
    },
    itemContainer: {
        backgroundColor: '#f9f9f9',
        padding: 15,
        marginBottom: 10,
        borderRadius: 5,
        elevation: 2,
    },
    titulo: {
        fontSize: 16,
        fontWeight: 'bold',
    },
    detalhes: {
        fontSize: 14,
        color: '#666',
    },
});

export default ListaProposicoes;
