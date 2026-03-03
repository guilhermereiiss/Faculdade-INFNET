
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import Home from "./screens/Home/index.jsx";
import BookDetails from "./screens/BookDetails/index.jsx";
import Inventory from "./screens/Inventory/index.jsx";



const Stack = createStackNavigator();

export default function App() {
    return (

        <NavigationContainer independent={true}>
            <Stack.Navigator>
                <Stack.Screen name="Home" component={Home} />
                <Stack.Screen name="Details" component={BookDetails} />
                <Stack.Screen name="Inventory" component={Inventory} />
            </Stack.Navigator>
        </NavigationContainer>

    );
}
