
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import TelaProdutos from './Produto.jsx';
import TelaCarrinho from './Carrinho.jsx';

const Stack = createStackNavigator();

const App = () => {
  return (
    <NavigationContainer independent={true}>
      <Stack.Navigator initialRouteName="Produtos">
        <Stack.Screen
          name="Produtos"
          component={TelaProdutos}
          options={{ title: 'Lista de Produtos' }}
        />
        <Stack.Screen
          name="Carrinho"
          component={TelaCarrinho}
          options={{ title: 'Carrinho de Compras' }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;
