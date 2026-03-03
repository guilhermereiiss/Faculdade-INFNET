
import { View, TextInput, StyleSheet } from 'react-native';

const SearchBar = ({ query, setQuery }) => {
    return (
        <View style={styles.container}>
            <TextInput
                style={styles.input}
                placeholder="Buscar notícias..."
                value={query}
                onChangeText={setQuery}
            />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        padding: 10,
    },
    input: {
        height: 40,
        borderColor: '#ccc',
        borderWidth: 1,
        borderRadius: 8,
        paddingHorizontal: 10,
    },
});

export default SearchBar;
