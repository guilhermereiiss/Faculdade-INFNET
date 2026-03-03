import { NavigationContainer} from "@react-navigation/native"
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs"
import Home from "./screens/Home/index.jsx";
import ATStack from "./screens/Tabs/ATStack.jsx";


const tab = createBottomTabNavigator()

function TabGroup() {
  return (
    <tab.Navigator>
      <tab.Screen name="Home" component={Home} />
      <tab.Screen name="AT" component={ATStack} />
    
    </tab.Navigator>
  );
}

export default function Navigation() {
  return (
    <NavigationContainer>
        <TabGroup />
    </NavigationContainer>
  );
}