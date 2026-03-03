
import { View, Text, StyleSheet } from 'react-native';

export default function DesacordoScreen({ route }) {
  const { userResponses, propositions } = route.params || {};

  const disagreed = propositions?.filter(prop => !userResponses[prop.id]);

  return (
    <View style={styles.container}>
      {disagreed?.map((prop, index) => (
        <Text key={index} style={styles.text}>{prop.statement}</Text>
      ))}
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 10 },
  text: { marginBottom: 10, fontSize: 16 },
});
