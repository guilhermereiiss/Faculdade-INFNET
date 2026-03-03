import { useState } from 'react';
import { Text, View, Button } from 'react-native';

export default function App() {
  const [selectedColor, setSelectedColor] = useState('');

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text style={{ fontSize: 24, marginBottom: 20 }}>
        {selectedColor ? `Você apertou: ${selectedColor}` : 'Aperte um botão'}
      </Text>
      
      <Button title="Vermelho" onPress={() => setSelectedColor('Vermelho')} color="red" />
      <Button title="Verde" onPress={() => setSelectedColor('Verde')} color="green" style={{ marginTop: 10 }} />
      <Button title="Azul" onPress={() => setSelectedColor('Azul')} color="blue" style={{ marginTop: 10 }} />
    </View>
  );
}
