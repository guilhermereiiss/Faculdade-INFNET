
import home from './components/home.jsx';
import pessoal from './components/pessoal.jsx';
import Academico from './components/Academico.jsx';
import experiencias from './components/Experiencias.jsx';
import idiomas from './components/Idiomas.jsx';
import softSkills from './components/Soft.jsx';

import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { NavigationContainer } from "@react-navigation/native"

const tab = createBottomTabNavigator()

function TabGroup() {
  return (
    <tab.Navigator >
      <tab.Screen name="Home" component={home} />
      <tab.Screen name="Pessoais" component={pessoal} />
      <tab.Screen name="Academico" component={Academico} />
      <tab.Screen name="Experiencias" component={experiencias} />
      <tab.Screen name="Idiomas" component={idiomas} />
      <tab.Screen name="Soft Skills" component={softSkills} />
    </tab.Navigator>
  );
}

export default function App() {
  return (
    <NavigationContainer independent={true}>
      <TabGroup />
    </NavigationContainer>
  );
}