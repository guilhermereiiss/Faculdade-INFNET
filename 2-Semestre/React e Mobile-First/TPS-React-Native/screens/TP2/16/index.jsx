
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import Perfil from './Perfil.jsx';
import FeedContatos from './FeedContatos.jsx';
import MinhasViagens from './MinhasViagens.jsx';
import Amigos from './Amigos.jsx';
import Configuracoes from './Configuracoes.jsx';
import DetalhesPostagem from './DetalhesPostagem.jsx';

const Drawer = createDrawerNavigator();

export default function App() {
  return (
    <NavigationContainer independent={true}>
      <Drawer.Navigator initialRouteName="FeedContatos">
        <Drawer.Screen name="Perfil" component={Perfil} />
        <Drawer.Screen name="Feed de Viagens" component={FeedContatos} />
        <Drawer.Screen name="Minhas Viagens" component={MinhasViagens} />
        <Drawer.Screen name="Amigos" component={Amigos} />
        <Drawer.Screen name="Configurações" component={Configuracoes} />
      </Drawer.Navigator>
    </NavigationContainer>
  );
}
