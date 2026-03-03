
import { View, Text, StyleSheet } from 'react-native';

const NewsCard = ({ news }) => {
    const editorias = Array.isArray(news.editorias) ? news.editorias.join(', ') : 'Sem editoria';

    return (
        <View style={styles.card}>
            <Text style={styles.title}>{news.titulo || 'Título indisponível'}</Text>
            <Text style={styles.details}>{news.data_publicacao || 'Data indisponível'}</Text>
            <Text style={styles.details}>{editorias}</Text>
        </View>
    );
};

const styles = StyleSheet.create({
    card: {
        padding: 15,
        marginVertical: 5,
        backgroundColor: '#fff',
        borderRadius: 8,
        elevation: 2,
    },
    title: {
        fontSize: 18,
        fontWeight: 'bold',
    },
    details: {
        fontSize: 14,
        color: '#666',
    },
});

export default NewsCard;
