import  { useState } from "react";
import { View, FlatList, StyleSheet } from "react-native";
import BookCard from "../../components/BookCard/index.jsx";

const Inventory = ({ navigation }) => {
  const [inventory, setInventory] = useState([]);

  return (
    <View style={styles.container}>
      <FlatList
        data={inventory}
        keyExtractor={(item) => item.key}
        renderItem={({ item }) => (
          <BookCard
            title={item.title}
            author={item.author_name?.[0] || "Unknown"}
            onPress={() => navigation.navigate("Details", { key: item.key })}
          />
        )}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
  },
});

export default Inventory;
