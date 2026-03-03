import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
    app: {
        flex: 1,
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: 20,
    },
    questionContainer: {
        width: '100%',
        maxWidth: 400,
    },
    optionsButton: {
        width: '100%',
        marginVertical: 10,
        padding: 15,
        borderWidth: 0,
        backgroundColor: '#3498db',
        color: 'white',
        fontSize: 16,
    },
    // light: {
    //     backgroundColor: '#f0f0f0',
    //     color: '#333',
    // },
    // dark: {
    //     backgroundColor: '#333',
    //     color: '#f0f0f0',
    // },
    optionsText: {
        borderWidth: 1,
        borderColor: 'black',
        padding: 1,
        margin: 5,
    },
});

export default styles;
