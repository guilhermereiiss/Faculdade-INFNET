
import { SafeAreaView, StyleSheet } from "react-native";
import PropositionListScreen from "./screens/ProposicaoListScreen/index.jsx";

const App = () => {
  return (
    <SafeAreaView style={styles.container}>
      <PropositionListScreen />
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#f8f8f8",
  },
});

export default App;
