import { View, Text, Image, StyleSheet } from 'react-native';

const academico = () => {
  return (
    <View style={styles.container}>

    <View style={styles.card}>
      <Image
        source={{ uri: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSu0MwNtLmn-Yg644qt0zO4zYcO0ziBsUFOQicd2CaVaLM1kVyyerVILZA83nmQ9U8Qs80&usqp=CAU' }} 
        style={styles.logo}
      />
      <Text style={styles.institutionName}>Escola Estadual ABC</Text>
      <Text style={styles.graduationYear}>Ano de Formação: 2018</Text>
      <Text style={styles.studyArea}>Área: Ensino Médio</Text>
    </View>


    <View style={styles.card}>
      <Image
        source={{ uri: 'https://faculdadeinfnet.com.br/wp-content/uploads/sites/10/2023/08/Modelos-Instagram-Infnet.png' }} // URL do logo da faculdade
        style={styles.logo}
      />
      <Text style={styles.institutionName}>Faculdade XYZ</Text>
      <Text style={styles.graduationYear}>Ano de Formação: 2023</Text>
      <Text style={styles.studyArea}>Área: Ciência da Computação</Text>
    </View>
  </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f4f4f4',
    alignItems: 'center',
    paddingTop: 20,
  },
  card: {
    backgroundColor: '#fff',
    borderRadius: 10,
    padding: 20,
    alignItems: 'center',
    width: '90%',
    marginVertical: 10,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 2 },
    shadowRadius: 8,
    elevation: 3,
  },
  logo: {
    width: 80,
    height: 80,
    resizeMode: 'contain',
    marginBottom: 10,
  },
  institutionName: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#333',
    marginVertical: 5,
  },
  graduationYear: {
    fontSize: 16,
    color: '#666',
    marginBottom: 5,
  },
  studyArea: {
    fontSize: 16,
    color: '#777',
  },
});


export default academico