
import { View, Text, StyleSheet } from "react-native";

const ProposicaoItem = ({ title, description }) => (
  <View style={styles.container}>
    <Text style={styles.title}>{title}</Text>
    <Text style={styles.description}>{description}</Text>
  </View>
);

const styles = StyleSheet.create({
  container: {
    padding: 16,
    borderBottomWidth: 1,
    borderColor: "#ddd",
  },
  title: {
    fontSize: 16,
    fontWeight: "bold",
  },
  description: {
    fontSize: 14,
    color: "#555",
  },
});

export default  ProposicaoItem;
