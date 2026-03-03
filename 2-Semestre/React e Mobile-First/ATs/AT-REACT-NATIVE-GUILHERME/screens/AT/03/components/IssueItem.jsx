
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const IssueItem = ({ issue }) => {
  return (
    <View style={styles.issueItem}>
      <Text style={styles.issueText}>{issue.title}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  issueItem: {
    padding: 15,
    marginVertical: 5,
    backgroundColor: '#05070D',
    borderRadius: 5,
  },
  issueText: {
    fontSize: 18,
    color: '#FFFF',
  },
});

export default IssueItem;
