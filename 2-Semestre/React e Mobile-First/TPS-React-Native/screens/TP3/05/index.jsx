import { useState } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { View, StyleSheet } from 'react-native';
import Questao from './components/Questao.jsx';
import BarraProgresso from './components/BarraProgresso.jsx';

const Stack = createStackNavigator();

const questoes = [
  { pergunta: 'Qual a capital da França?', opcoes: ['Paris', 'Roma', 'Berlim', 'Lisboa'] },
  { pergunta: '2 + 2 é igual a?', opcoes: ['3', '4', '5', '6'] },
  { pergunta: 'Qual o maior planeta do Sistema Solar?', opcoes: ['Terra', 'Marte', 'Júpiter', 'Vênus'] },
  { pergunta: 'Qual é o elemento químico com símbolo H?', opcoes: ['Hélio', 'Hidrogênio', 'Cálcio', 'Carbono'] },
  { pergunta: 'Quem pintou a Mona Lisa?', opcoes: ['Van Gogh', 'Leonardo da Vinci', 'Pablo Picasso', 'Michelangelo'] },
  { pergunta: 'Qual é o animal terrestre mais rápido do mundo?', opcoes: ['Leão', 'Leopardo', 'Guepardo', 'Antílope'] },
  { pergunta: 'Em que ano o homem pisou na Lua pela primeira vez?', opcoes: ['1965', '1969', '1972', '1980'] },
  { pergunta: 'Qual é o país com maior extensão territorial do mundo?', opcoes: ['China', 'Rússia', 'Canadá', 'Estados Unidos'] },
  { pergunta: 'Quantos continentes existem na Terra?', opcoes: ['5', '6', '7', '8'] },
  { pergunta: 'Quem escreveu "Dom Quixote"?', opcoes: ['William Shakespeare', 'Miguel de Cervantes', 'J.K. Rowling', 'Gabriel García Márquez'] },
];


export default function App() {
  const [progresso, setProgresso] = useState(0);

  return (
    <NavigationContainer independent={true}>
      <Stack.Navigator screenOptions={{ headerShown: false }}>
        {questoes.map((questao, index) => (
          <Stack.Screen key={index} name={`Questao${index}`}>
            {() => (
              <View style={styles.container}>
                <BarraProgresso progresso={(index + 1) / questoes.length} />
                <Questao
                  pergunta={questao.pergunta}
                  opcoes={questao.opcoes}
                  onProximo={() => {
                    setProgresso((index + 1) / questoes.length);
                  }}
                  proximaTela={`Questao${index + 1}`}
                />
              </View>
            )}
          </Stack.Screen>
        ))}
      </Stack.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    backgroundColor: '#f9f9f9',
  },
});
