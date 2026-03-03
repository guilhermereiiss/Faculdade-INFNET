import React, { useEffect, useState } from 'react';
import { View, Text, FlatList, StyleSheet, RefreshControl, Modal, TextInput, TouchableOpacity, Alert, ScrollView } from 'react-native';
import { getIssues, getRepos } from '../api/githubApi'; 
import IssueItem from '../components/IssueItem';
import axios from 'axios'; 

const IssuesScreen = ({ route }) => {
  const { token } = route.params;
  const [repos, setRepos] = useState([]); 
  const [issues, setIssues] = useState([]); 
  const [refreshing, setRefreshing] = useState(false);
  
  const [modalVisible, setModalVisible] = useState(false);
  const [repoName, setRepoName] = useState('');
  const [issueDescription, setIssueDescription] = useState('');

  useEffect(() => {
    fetchRepos(); 
  }, []);

  const fetchRepos = async () => {
    const reposData = await getRepos(token); 
    setRepos(reposData);
  };

  const fetchIssuesForRepo = async (repoName) => {
    const issuesData = await getIssues(token, repoName); 
    setIssues(issuesData);
  };

  const onRefresh = async () => {
    setRefreshing(true);
    await fetchRepos();
    setRefreshing(false);
  };

  const handleSubmit = async () => {
    if (!repoName || !issueDescription) {
      Alert.alert('Erro', 'Preencha todos os campos.');
      return;
    }

    try {
      const response = await axios.post(
        `https://api.github.com/repos/{owner}/${repoName}/issues`,
        {
          title: repoName,
          body: issueDescription,
        },
        {
          headers: {
            Authorization: `token ${token}`,
          },
        }
      );

      if (response.status === 201) {
        Alert.alert('Sucesso', 'Issue criada com sucesso!');
        setModalVisible(false);
        setRepoName('');
        setIssueDescription('');
      }
    } catch (error) {
      console.error(error);
      Alert.alert('Erro', 'Falha ao criar a issue. Tente novamente.');
    }
  };

  return (
    <ScrollView style={styles.container}>
      <FlatList
        data={repos}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <View style={styles.repoCard}>
            <Text style={styles.repoName}>{item.name}</Text>
            <TouchableOpacity
              style={styles.button}
              onPress={() => fetchIssuesForRepo(item.name)} 
            >
              <Text style={styles.buttonText}>Ver Issues</Text>
            </TouchableOpacity>

           
            {issues.length > 0 && (
              <FlatList
                data={issues}
                keyExtractor={(issue) => issue.id.toString()}
                renderItem={({ item }) => (
                  <IssueItem issue={item} />
                )}
                style={styles.issuesList}
              />
            )}
          </View>
        )}
        refreshControl={<RefreshControl refreshing={refreshing} onRefresh={onRefresh} />}
        contentContainerStyle={styles.listContainer}
      />

      
      <TouchableOpacity style={styles.button} onPress={() => setModalVisible(true)}>
        <Text style={styles.buttonText}>Adicionar Issue</Text>
      </TouchableOpacity>

      
      <Modal
        animationType="slide"
        transparent={true}
        visible={modalVisible}
        onRequestClose={() => setModalVisible(false)}
      >
        <View style={styles.modalOverlay}>
          <View style={styles.modalContainer}>
            <Text style={styles.modalTitle}>Adicionar Nova Issue</Text>
            <TextInput
              style={styles.input}
              placeholder="Nome do Repositório"
              value={repoName}
              onChangeText={setRepoName}
            />
            <TextInput
              style={styles.input}
              placeholder="Descrição da Issue"
              value={issueDescription}
              onChangeText={setIssueDescription}
              multiline
            />
            <View style={styles.modalButtons}>
              <TouchableOpacity style={styles.button} onPress={handleSubmit}>
                <Text style={styles.buttonText}>Submeter</Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={styles.button}
                onPress={() => setModalVisible(false)}
              >
                <Text style={styles.buttonText}>Cancelar</Text>
              </TouchableOpacity>
            </View>
          </View>
        </View>
      </Modal>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#101526',
    padding: 10,
  },
  repoCard: {
    backgroundColor: '#1A2637',
    padding: 20,
    borderRadius: 10,
    marginBottom: 20,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 6,
    elevation: 5,
  },
  repoName: {
    fontSize: 18,
    color: '#FFF',
    fontWeight: 'bold',
    marginBottom: 10,
  },
  issuesList: {
    marginTop: 10,
  },
  listContainer: {
    marginBottom: 20,
  },
  button: {
    backgroundColor: '#1A6DD9',
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 5,
    alignItems: 'center',
    marginTop: 10,
  },
  buttonText: {
    color: '#FFFF',
    fontSize: 18,
    fontWeight: 'bold',
  },
  modalOverlay: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
  },
  modalContainer: {
    backgroundColor: '#1A2637',
    padding: 20,
    borderRadius: 10,
    width: '80%',
    alignItems: 'center',
  },
  modalTitle: {
    fontSize: 20,
    color: '#FFF',
    fontWeight: 'bold',
    marginBottom: 20,
  },
  input: {
    width: '100%',
    padding: 10,
    marginBottom: 20,
    backgroundColor: '#2C3E50',
    borderRadius: 5,
    color: '#FFF',
    fontSize: 16,
  },
  modalButtons: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    width: '100%',
  },
});

export default IssuesScreen;


