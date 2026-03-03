
import { View, Text, StyleSheet } from 'react-native';

const RepoItem = ({ repo }) => {
  return (
    <View style={styles.repoItem}>
      <Text style={styles.repoText}>{repo.name}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  repoItem: {
    padding: 15,
    marginVertical: 5,
    backgroundColor: '#05070D',
    borderRadius: 5,
  },
  repoText: {
    fontSize: 18,
    color: '#FFFF',
  },
});

export default RepoItem;
