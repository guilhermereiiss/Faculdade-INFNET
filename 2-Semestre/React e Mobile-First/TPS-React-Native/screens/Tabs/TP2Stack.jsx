import { createStackNavigator } from "@react-navigation/stack";
import TP2 from "../TP2/index.jsx";
import TP2_01 from "../TP2/01/index.jsx";
import TP2_02 from "../TP2/02/index.jsx";
import TP2_03 from "../TP2/03/index.jsx";
import TP2_04 from "../TP2/04/index.jsx";
import TP2_05 from "../TP2/05/index.jsx";
import TP2_06 from "../TP2/06/index.jsx";
import TP2_07 from "../TP2/07/index.jsx";
import TP2_08 from "../TP2/08/index.jsx";
import TP2_09 from "../TP2/09/index.jsx";
import TP2_10 from "../TP2/10/index.jsx";
import TP2_11 from "../TP2/11/index.jsx";
import TP2_12 from "../TP2/12/index.jsx";
import TP2_13 from "../TP2/13/index.jsx";
import TP2_14 from "../TP2/14/index.jsx";
import TP2_15 from "../TP2/15/index.jsx";
import TP2_16 from "../TP2/16/index.jsx";

const Stack = createStackNavigator();

export default function TP2Stack() {
  return (
    <Stack.Navigator>
      <Stack.Screen name="Exercícios:" component={TP2} />
      <Stack.Screen name="Exercício - 1" component={TP2_01} />
      <Stack.Screen name="Exercício - 2" component={TP2_02} />
      <Stack.Screen name="Exercício - 3" component={TP2_03} />
      <Stack.Screen name="Exercício - 4" component={TP2_04} />
      <Stack.Screen name="Exercício - 5" component={TP2_05} />
      <Stack.Screen name="Exercício - 6" component={TP2_06} />
      <Stack.Screen name="Exercício - 7" component={TP2_07} />
      <Stack.Screen name="Exercício - 8" component={TP2_08} />
      <Stack.Screen name="Exercício - 9" component={TP2_09} />
      <Stack.Screen name="Exercício - 10" component={TP2_10} />
      <Stack.Screen name="Exercício - 11" component={TP2_11} />
      <Stack.Screen name="Exercício - 12" component={TP2_12} />
      <Stack.Screen name="Exercício - 13" component={TP2_13} />
      <Stack.Screen name="Exercício - 14" component={TP2_14} />
      <Stack.Screen name="Exercício - 15" component={TP2_15} />
      <Stack.Screen name="Exercício - 16" component={TP2_16} />
    </Stack.Navigator>
  );
}
