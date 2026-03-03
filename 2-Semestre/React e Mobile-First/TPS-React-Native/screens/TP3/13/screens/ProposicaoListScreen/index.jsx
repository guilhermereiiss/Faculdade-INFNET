import  { useState, useEffect } from "react";
import { View, FlatList, StyleSheet, Text } from "react-native";


import  ProposicaoItem from "../../Components/ProposicaoItem/index.jsx";
import { fetchProposiçao } from "../../services/index.jsx";

const PropositionListScreen = () => {
  const [propositions, setPropositions] = useState([]);
  const [refreshing, setRefreshing] = useState(false);

  const loadProposicao = async () => {
    const data = await fetchProposiçao();
    setPropositions(data);
  };

  const handleRefresh = async () => {
    setRefreshing(true);
    await loadProposicao();
    setRefreshing(false);
  };

  useEffect(() => {
    loadProposicao();
  }, []);

  return (
    <View style={styles.container}>
      {propositions.length === 0 ? (
        <Text style={styles.message}>Nenhuma proposição encontrada.</Text>
      ) : (
        <FlatList
          data={propositions}
          keyExtractor={(item) => item.id.toString()}
          renderItem={({ item }) => (
            <ProposicaoItem title={item.titulo} description={item.descricaoTipo} />
          )}
          refreshing={refreshing}
          onRefresh={handleRefresh}
        />
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    backgroundColor: "#fff",
  },
  message: {
    fontSize: 16,
    textAlign: "center",
    marginTop: 20,
  },
});

export default PropositionListScreen;
