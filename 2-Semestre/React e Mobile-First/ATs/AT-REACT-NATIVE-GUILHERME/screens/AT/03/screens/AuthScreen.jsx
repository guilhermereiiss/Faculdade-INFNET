
import  { useState } from 'react';
import { TextInput, Button, View, Text, StyleSheet } from 'react-native';

const AuthScreen = ({ navigation }) => {
  const [token, setToken] = useState('');

  const handleLogin = () => {
    if (token) {
      navigation.navigate('UserInfo', { token });
    } else {
      alert('Por favor, insira um token válido');
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Digite seu Token do GitHub</Text>
      <TextInput
        value={token}
        onChangeText={setToken}
        placeholder="Token"
        placeholderTextColor="#2291F2"
        style={styles.input}
      />
      <Button title="Login" onPress={handleLogin} color="#1A6DD9" />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#101526',
  },
  title: {
    fontSize: 24,
    color: '#FFFF',
    marginBottom: 20,
  },
  input: {
    width: '80%',
    height: 40,
    backgroundColor: '#05070D',
    borderColor: '#2291F2',
    borderWidth: 1,
    color: '#FFFF',
    paddingLeft: 10,
    marginBottom: 20,
  },
});

export default AuthScreen;
