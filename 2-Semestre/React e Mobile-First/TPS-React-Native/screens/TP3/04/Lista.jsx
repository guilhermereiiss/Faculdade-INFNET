import { SectionList, Text, View, StyleSheet } from 'react-native';

const Lista = ({ categorias }) => {
  const renderizarItem = ({ item }) => (
    <View style={styles.cardItem}>
      <Text style={styles.textoItem}>{item}</Text>
    </View>
  );

  const renderizarCabecalho = ({ section }) => (
    <View style={styles.cabecalho}>
      <Text style={styles.textoCabecalho}>{section.title}</Text>
    </View>
  );

  return (
    <SectionList
      sections={categorias}
      keyExtractor={(item, index) => item + index}
      renderItem={renderizarItem}
      renderSectionHeader={renderizarCabecalho}
      contentContainerStyle={styles.containerLista}
    />
  );
};

const styles = StyleSheet.create({
  containerLista: {
    paddingVertical: 12,
  },
  cabecalho: {
    backgroundColor: '#0288d1',
    padding: 12,
    borderRadius: 6,
    marginVertical: 6,
  },
  textoCabecalho: {
    fontSize: 20,
    color: '#ffffff',
    fontWeight: '700',
  },
  cardItem: {
    backgroundColor: '#ffffff',
    padding: 15,
    marginVertical: 6,
    borderRadius: 10,
    elevation: 2,
    shadowColor: '#666',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.3,
    shadowRadius: 4,
  },
  textoItem: {
    fontSize: 16,
    color: '#1a1a1a',
  },
});

export default Lista;
