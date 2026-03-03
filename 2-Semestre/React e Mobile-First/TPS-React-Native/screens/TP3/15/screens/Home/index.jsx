import  { useState } from "react";
import { View, FlatList, StyleSheet } from "react-native";
import SearchBar from "../../components/SearchBar/index.jsx";
import BookCard from "../../components/BookCard/index.jsx";
import { searchBooks } from "../../services/index.jsx";

const Home = ({ navigation }) => {
  const [query, setQuery] = useState("");
  const [books, setBooks] = useState([]);

  const handleSearch = async () => {
    const results = await searchBooks(query);
    setBooks(results.docs || []);
  };

  return (
    <View style={styles.container}>
      <SearchBar
        value={query}
        onChangeText={setQuery}
        onSubmit={handleSearch}
      />
      <FlatList
        data={books}
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

export default Home;
