import { View, Picker, StyleSheet } from 'react-native';

export default function OrdenarProdutos({ setOrdenacao }) {
    return (
        <View style={styles.pickerContainer}>
            <Picker
                selectedValue={'asc'}
                onValueChange={(itemValue) => setOrdenacao(itemValue)}
                mode="dropdown"
            >
                <Picker.Item label="Nome Crescente" value="asc" />
                <Picker.Item label="Nome Decrescente" value="desc" />
            </Picker>
        </View>
    );
}

const styles = StyleSheet.create({
    pickerContainer: {
        margin: 10,
    },
});