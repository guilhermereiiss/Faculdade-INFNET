
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import ListaPostagens from './ListaPostagens.jsx';
import DetalhesPostagem from './DetalhesPostagem.jsx';

const Stack = createStackNavigator();

export default function App() {
    return (
        <NavigationContainer independent={true}>
            <Stack.Navigator initialRouteName="ListaPostagens">
                <Stack.Screen
                    name="ListaPostagens"
                    component={ListaPostagens}
                    options={{ title: 'Postagens' }}
                />
                <Stack.Screen
                    name="DetalhesPostagem"
                    component={DetalhesPostagem}
                    options={{ title: 'Detalhes da Postagem' }}
                />
            </Stack.Navigator>
        </NavigationContainer>
    );
}

