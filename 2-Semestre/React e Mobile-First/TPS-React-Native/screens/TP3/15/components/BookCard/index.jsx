
import { View, Text, StyleSheet, TouchableOpacity } from "react-native";

const BookCard = ({ title, author, onPress }) => (
  <TouchableOpacity onPress={onPress} style={styles.card}>
    <Text style={styles.title}>{title}</Text>
    <Text style={styles.author}>{author}</Text>
  </TouchableOpacity>
);

const styles = StyleSheet.create({
  card: {
    padding: 16,
    marginVertical: 8,
    backgroundColor: "#f5f5f5",
    borderRadius: 8,
  },
  title: {
    fontWeight: "bold",
    fontSize: 16,
  },
  author: {
    color: "#666",
    marginTop: 4,
  },
});

export default BookCard;
