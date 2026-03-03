import { View, Text, StyleSheet, Image, ScrollView } from 'react-native';

const experiencias = () => {
  return (
    <ScrollView>
    <View style={styles.container}>
    <View style={styles.card}>
      <Image
        source={{ uri: 'https://www.stickersdevs.com.br/wp-content/uploads/2021/03/amazon-logo-sticker-adesivo.jpg' }} 
        style={styles.logo}
      />
      <Text style={styles.companyName}>Amazon</Text>
      <Text style={styles.jobTitle}>Cargo: Desenvolvedor Front-End</Text>
      <Text style={styles.workPeriod}>Período: Jan 2020 - Dez 2022</Text>
      <Text style={styles.jobDescription}>
        Responsável pelo desenvolvimento de interfaces responsivas e manutenção de sistemas web.
      </Text>
    </View>

    
    <View style={styles.card}>
      <Image
        source={{ uri: 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1200px-Google_2015_logo.svg.png' }} 
        style={styles.logo}
      />
      <Text style={styles.companyName}>Google</Text>
      <Text style={styles.jobTitle}>Cargo: Desenvolvedor Full Stack</Text>
      <Text style={styles.workPeriod}>Período: Mar 2018 - Dez 2019</Text>
      <Text style={styles.jobDescription}>
        Atuei no desenvolvimento de soluções para o backend e integração com plataformas externas.
      </Text>
    </View>
  </View>
  </ScrollView>
  )
}

export default experiencias

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
  companyName: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#333',
    marginVertical: 5,
  },
  jobTitle: {
    fontSize: 16,
    color: '#666',
    marginBottom: 5,
  },
  workPeriod: {
    fontSize: 16,
    color: '#777',
    marginBottom: 10,
  },
  jobDescription: {
    fontSize: 14,
    color: '#777',
    textAlign: 'center',
  },
});


