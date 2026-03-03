
import { View, Text, StyleSheet } from 'react-native';

const LoadingIndicator = ({ progress }) => (
    <View style={styles.container}>
        <Text style={styles.text}>Carregando... {Math.round(progress * 100)}%</Text>
        <View style={styles.progressBarContainer}>
            <View style={[styles.progressBar, { width: `${progress * 100}%` }]} />
        </View>
    </View>
);

const styles = StyleSheet.create({
    container: {
        marginVertical: 10,
        alignItems: 'center',
        width: '80%',
    },
    text: {
        marginBottom: 5,
        fontSize: 16,
    },
    progressBarContainer: {
        width: '100%',
        height: 10,
        backgroundColor: '#ddd',
        borderRadius: 5,
        overflow: 'hidden',
    },
    progressBar: {
        height: '100%',
        backgroundColor: '#6200ee',
    },
});

export default LoadingIndicator;
