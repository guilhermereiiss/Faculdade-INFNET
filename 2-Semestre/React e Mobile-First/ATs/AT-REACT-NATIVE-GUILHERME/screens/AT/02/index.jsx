
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from './screens/HomeScreen';
import ImageDetailsScreen from './screens/ImageDetailsScreen';

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer independent={true}>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="ImageDetails" component={ImageDetailsScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
