import { useState } from 'react';
import { View, Text, Button } from 'react-native';

export default function Preferencia({ itens, respostas, setRespostas, alternarTela }) {
  const [indiceAtual, setIndiceAtual] = useState(0); 

  const responder = (gosta) => {
    const itemAtual = itens[indiceAtual];
    setRespostas({ ...respostas, [itemAtual]: gosta });

    if (indiceAtual < itens.length - 1) {
      setIndiceAtual(indiceAtual + 1);
    } else {
      alternarTela(); 
    }
  };

  return (
    <View>
      <Text style={{ fontSize: 24, marginBottom: 10 }}>Você gosta de:</Text>
      <Text style={{ fontSize: 18, marginBottom: 20 }}>{itens[indiceAtual]}</Text>
      <Button title="Sim" onPress={() => responder(true)} />
      <Button title="Não" onPress={() => responder(false)} />
    </View>
  );
}
