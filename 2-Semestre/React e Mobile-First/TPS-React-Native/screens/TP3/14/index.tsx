import  { useState } from 'react';
import { NavigationContainer, NavigationIndependentTree } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import HomeScreen from './screens/Home/index.jsx';
import AcordoScreen from './screens/Acordo/index.jsx';
import DesacordoScreen from './screens/Desacordo/index.jsx';

const Tab = createBottomTabNavigator();

export default function App() {
  const [propositions, setPropositions] = useState([]);
  const [userResponses, setUserResponses] = useState({});

  return (
    <NavigationContainer independent={true}>
      <Tab.Navigator screenOptions={{ headerShown: false }}>
        <Tab.Screen name="Proposições">
          {() => (
            <HomeScreen
              propositions={propositions}
              setPropositions={setPropositions}
              userResponses={userResponses}
              setUserResponses={setUserResponses}
            />
          )}
        </Tab.Screen>
        <Tab.Screen name="Concordei">
          {() => (
            <AcordoScreen
              propositions={propositions}
              userResponses={userResponses}
            />
          )}
        </Tab.Screen>
        <Tab.Screen name="Discordei">
          {() => (
            <DesacordoScreen
              propositions={propositions}
              userResponses={userResponses}
            />
          )}
        </Tab.Screen>
      </Tab.Navigator>
    </NavigationContainer>
  );
}