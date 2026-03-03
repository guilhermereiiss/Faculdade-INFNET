
import { View, Text, StyleSheet } from 'react-native';

export default function AcordoScreen({ route }) {
  const { userResponses, propositions } = route.params || {};

  const agreed = propositions?.filter(prop => userResponses[prop.id]);

  return (
    <View style={styles.container}>
      {agreed?.map((prop, index) => (
        <Text key={index} style={styles.text}>{prop.statement}</Text>
      ))}
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 10 },
  text: { marginBottom: 10, fontSize: 16 },
});
