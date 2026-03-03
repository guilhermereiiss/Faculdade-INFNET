
import { View, Text, StyleSheet } from 'react-native';

const IssueDetailsScreen = ({ route }) => {
  const { issue } = route.params; 

  return (
    <View style={styles.container}>
      <Text style={styles.title}>{issue.title}</Text>
      <Text style={styles.description}>{issue.body}</Text>
      <Text style={styles.details}>Created by: {issue.user.login}</Text>
      <Text style={styles.details}>Labels: {issue.labels.map(label => label.name).join(', ')}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#101526',
  },
  title: {
    fontSize: 24,
    color: '#FFFF',
    fontWeight: 'bold',
  },
  description: {
    fontSize: 18,
    color: '#FFFF',
    marginVertical: 10,
  },
  details: {
    fontSize: 16,
    color: '#2291F2',
    marginBottom: 5,
  },
});

export default IssueDetailsScreen;
