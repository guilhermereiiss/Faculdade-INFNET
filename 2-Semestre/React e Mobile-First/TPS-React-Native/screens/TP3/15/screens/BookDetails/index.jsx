import  { useEffect, useState } from "react";
import { View, Text, StyleSheet } from "react-native";
import { fetchBookDetails } from "../../services";

const BookDetails = ({ route }) => {
  const { key } = route.params;
  const [details, setDetails] = useState(null);

  useEffect(() => {
    const loadDetails = async () => {
      const data = await fetchBookDetails(key);
      setDetails(data);
    };
    loadDetails();
  }, [key]);

  if (!details) {
    return <Text>Loading...</Text>;
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>{details.title}</Text>
      <Text>Author: {details.by_statement || "Unknown"}</Text>
      <Text>Description: {details.description || "No description available"}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 16,
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 16,
  },
});

export default BookDetails;
