import { useEffect, useState } from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import axios from 'axios';

export default function HomeScreen({ navigation }) {
  const [propositions, setPropositions] = useState([]);
  const [userResponses, setUserResponses] = useState({});

  useEffect(() => {
    axios.get('https://jsonplaceholder.typicode.com/posts')
      .then(response => {
        const formatted = response.data.map(post => ({
          id: post.id,
          statement: post.title,
          agreeCount: Math.floor(Math.random() * 100),
          disagreeCount: Math.floor(Math.random() * 100),
        }));
        setPropositions(formatted);
      })
      .catch(error => console.error(error));
  }, []);

  const handleResponse = (id, agree) => {
    setUserResponses(prev => ({ ...prev, [id]: agree }));
    setPropositions(prev =>
      prev.map(prop =>
        prop.id === id
          ? {
              ...prop,
              agreeCount: agree ? prop.agreeCount + 1 : prop.agreeCount,
              disagreeCount: !agree ? prop.disagreeCount + 1 : prop.disagreeCount,
            }
          : prop
      )
    );
  };

  return (
    <View style={styles.container}>
      {propositions.map((prop, index) => (
        <View key={index} style={styles.card}>
          <Text style={styles.text}>{prop.statement}</Text>
          <Button title="Concordo" onPress={() => handleResponse(prop.id, true)} />
          <Button title="Discordo" onPress={() => handleResponse(prop.id, false)} />
          <Text>Concordam: {prop.agreeCount} | Discordam: {prop.disagreeCount}</Text>
        </View>
      ))}
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 10 },
  card: { marginBottom: 20, padding: 10, borderWidth: 1, borderRadius: 5 },
  text: { marginBottom: 10, fontSize: 16 },
});
