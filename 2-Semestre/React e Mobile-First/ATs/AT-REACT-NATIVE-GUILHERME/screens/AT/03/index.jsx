

import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import AuthScreen from './screens/AuthScreen';
import UserInfoScreen from './screens/UserInfoScreen';
import ReposScreen from './screens/ReposScreen';
import IssuesScreen from './screens/IssuesScreen';
import RepoDetailsScreen from './screens/RepoDetailsScreen';
import IssueDetailsScreen from './screens/IssuesScreen';    
import IssueItem from './components/IssueItem';

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer independent={true}>
      <Stack.Navigator initialRouteName="Auth">
        <Stack.Screen
          name="Auth"
          component={AuthScreen}
          options={{ headerStyle: { backgroundColor: '#101526' }, headerTintColor: '#FFFF' }}
        />
        <Stack.Screen
          name="UserInfo"
          component={UserInfoScreen}
          options={{ headerStyle: { backgroundColor: '#1A6DD9' }, headerTintColor: '#FFFF' }}
        />
        <Stack.Screen
          name="Repos"
          component={ReposScreen}
          options={{ headerStyle: { backgroundColor: '#1A6DD9' }, headerTintColor: '#FFFF' }}
        />
        <Stack.Screen
          name="Issues"
          component={IssuesScreen}
          options={{ headerStyle: { backgroundColor: '#1A6DD9' }, headerTintColor: '#FFFF' }}
        />
        <Stack.Screen
          name="RepoDetails"
          component={RepoDetailsScreen}
          options={{ headerStyle: { backgroundColor: '#1A6DD9' }, headerTintColor: '#FFFF' }}
        />
         <Stack.Screen
          name="IssueItem"
          component={IssueItem}
          options={{ headerStyle: { backgroundColor: '#1A6DD9' }, headerTintColor: '#FFFF' }}
        /> 
        <Stack.Screen
        name="IssueDetails"
        component={IssueDetailsScreen}
        options={{ headerStyle: { backgroundColor: '#1A6DD9' }, headerTintColor: '#FFFF' }}
      />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
