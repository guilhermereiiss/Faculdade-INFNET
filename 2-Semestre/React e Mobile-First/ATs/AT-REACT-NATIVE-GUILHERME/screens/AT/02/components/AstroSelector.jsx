import { View, Picker, StyleSheet } from 'react-native';

const AstroSelector = ({ onAstroChange }) => (
    <View style={styles.selectorContainer}>
        <Picker
            selectedValue="earth"
            onValueChange={(value) => onAstroChange(value)}
            style={styles.picker}
        >
            <Picker.Item label="Terra" value="earth" />
            <Picker.Item label="Lua" value="moon" />
            <Picker.Item label="Sol" value="sun" />
            <Picker.Item label="Marte" value="mars" />
            <Picker.Item label="Júpiter" value="jupiter" />
        </Picker>
    </View>
);

const styles = StyleSheet.create({
    selectorContainer: {
        marginVertical: 10,
        backgroundColor: '#05070D',  
        padding: 10,  
        borderRadius: 8,  
    },
    picker: {
        height: 50,
        color: 'black',  
        borderColor: '#1A6DD9', 
        borderWidth: 1,  
        borderRadius: 5, 
    },
});

export default AstroSelector;
