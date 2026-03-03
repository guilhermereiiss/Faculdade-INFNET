import { View, Text, StyleSheet, ScrollView } from 'react-native';

const softSkills = () => {
  return (
    <ScrollView>
      <View style={styles.container}>
        <View style={styles.card}>
          <Text style={styles.skillName}>Comunicação</Text>
          <Text style={styles.skillDescription}>
            Habilidade para transmitir informações de forma clara e eficiente, tanto verbalmente quanto por escrito.
          </Text>
          <Text style={styles.skillLevel}>Nível: Avançado</Text>
        </View>


        <View style={styles.card}>
          <Text style={styles.skillName}>Trabalho em Equipe</Text>
          <Text style={styles.skillDescription}>
            Capacidade de trabalhar bem com outras pessoas, contribuindo para o sucesso coletivo.
          </Text>
          <Text style={styles.skillLevel}>Nível: Intermediário</Text>
        </View>


        <View style={styles.card}>
          <Text style={styles.skillName}>Gestão de Tempo</Text>
          <Text style={styles.skillDescription}>
            Habilidade de organizar e priorizar tarefas para cumprir prazos e metas de forma eficiente.
          </Text>
          <Text style={styles.skillLevel}>Nível: Avançado</Text>
        </View>

        <View style={styles.card}>
          <Text style={styles.skillName}>Resolução de Problemas</Text>
          <Text style={styles.skillDescription}>
            Capacidade de identificar problemas e encontrar soluções eficazes e criativas.
          </Text>
          <Text style={styles.skillLevel}>Nível: Intermediário</Text>
        </View>

        <View style={styles.card}>
          <Text style={styles.skillName}>Liderança</Text>
          <Text style={styles.skillDescription}>
            Habilidade de motivar, inspirar e orientar equipes para alcançar objetivos comuns.
          </Text>
          <Text style={styles.skillLevel}>Nível: Intermediário</Text>
        </View>
      </View>
    </ScrollView>
  )
}

export default softSkills

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
    width: '90%',
    marginVertical: 10,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 2 },
    shadowRadius: 8,
    elevation: 3,
  },
  skillName: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 5,
  },
  skillDescription: {
    fontSize: 16,
    color: '#666',
    marginBottom: 10,
  },
  skillLevel: {
    fontSize: 16,
    color: '#777',
  },
});

