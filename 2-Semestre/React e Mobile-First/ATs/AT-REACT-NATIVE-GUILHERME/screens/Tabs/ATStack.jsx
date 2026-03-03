import { createStackNavigator } from "@react-navigation/stack";
import AT from "../AT/index.jsx";
import AT_01 from "../AT/01/index.jsx";
import AT_02 from "../AT/02/index.jsx";
import AT_03 from "../AT/03/index.jsx";


const Stack = createStackNavigator();

export default function TP1Stack() {
  return (
    <Stack.Navigator>
      <Stack.Screen name="Exercícios:" component={AT} />
      <Stack.Screen name="Exercício - 1" component={AT_01} />
      <Stack.Screen name="Exercício - 2" component={AT_02} />
      <Stack.Screen name="Exercício - 3" component={AT_03} />
    </Stack.Navigator>
  );
}
