
import { NavigationContainer } from '@react-navigation/native';
import NewsListScreen from './components/NewsListScreen';

export default function App() {
  return (
  
      <NavigationContainer independent={true}>
        <NewsListScreen />
      </NavigationContainer>
  
  );
}
