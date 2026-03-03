
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import LoginScreen from './screens/LoginScreen.jsx';
import TransacaoListScreen from './screens/TransacaoListScreen.jsx'; 

const Stack = createStackNavigator();

export default function AppNavigator() {
  return (
    <NavigationContainer independent={true}>
      <Stack.Navigator initialRouteName="Login" screenOptions={{ headerShown: false }}>
        <Stack.Screen name="Login" component={LoginScreen} />
        <Stack.Screen name="Transacoes" component={TransacaoListScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
