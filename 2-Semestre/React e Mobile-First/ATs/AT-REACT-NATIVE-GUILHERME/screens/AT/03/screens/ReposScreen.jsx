import { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity } from 'react-native';
import RNPickerSelect from 'react-native-picker-select';
import { getRepos } from '../api/githubApi';

const ReposScreen = ({ route, navigation }) => {
  const { token } = route.params;
  const [repos, setRepos] = useState([]);
  const [filteredRepos, setFilteredRepos] = useState([]);
  const [visibilityFilter, setVisibilityFilter] = useState('all'); 
  const [sortOption, setSortOption] = useState('az'); 

  
  const sortRepos = (repos, option) => {
    switch (option) {
      case 'az':
        return repos.sort((a, b) => a.name.localeCompare(b.name)); 
      case 'za':
        return repos.sort((a, b) => b.name.localeCompare(a.name)); 
      case 'newest':
        return repos.sort((a, b) => new Date(b.created_at) - new Date(a.created_at)); 
      case 'oldest':
        return repos.sort((a, b) => new Date(a.created_at) - new Date(b.created_at)); 
      default:
        return repos;
    }
  };

  
  const filterRepos = (repos, visibility) => {
    if (visibility === 'all') {
      return repos;
    }
    return repos.filter(repo => repo.private === (visibility === 'private'));
  };

  useEffect(() => {
    const fetchRepos = async () => {
      const data = await getRepos(token);
      const filtered = filterRepos(data, visibilityFilter); 
      const sorted = sortRepos(filtered, sortOption); 
      setRepos(sorted);
      setFilteredRepos(sorted); 
    };

    fetchRepos();
  }, [token, visibilityFilter, sortOption]);

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <View style={styles.filterContainer}>
        <Text style={styles.filterLabel}>Filtrar por visibilidade:</Text>
        <RNPickerSelect
          onValueChange={(value) => setVisibilityFilter(value)}
          items={[
            { label: 'Todos', value: 'all' },
            { label: 'Públicos', value: 'public' },
            { label: 'Privados', value: 'private' },
          ]}
          style={pickerSelectStyles}
          value={visibilityFilter}
          useNativeAndroidPickerStyle={false} 
        />
        <Text style={styles.filterLabel}>Ordenar por:</Text>
        <RNPickerSelect
          onValueChange={(value) => setSortOption(value)}
          items={[
            { label: 'A-Z', value: 'az' },
            { label: 'Z-A', value: 'za' },
            { label: 'Mais recentes', value: 'newest' },
            { label: 'Mais antigos', value: 'oldest' },
          ]}
          style={pickerSelectStyles}
          value={sortOption}
          useNativeAndroidPickerStyle={false}
        />
      </View>

      {repos.length === 0 ? (
        <Text style={styles.loadingText}>Carregando Repositórios...</Text>
      ) : (
        repos.map((repo) => (
          <TouchableOpacity
            key={repo.id}
            style={styles.repoCard}
            onPress={() => navigation.navigate('RepoDetails', { repo })}
          >
            <Text style={styles.repoName}>{repo.name}</Text>
            {repo.description ? (
              <Text style={styles.repoDescription}>{repo.description}</Text>
            ) : (
              <Text style={styles.noDescription}>Sem descrição disponível</Text>
            )}
          </TouchableOpacity>
        ))
      )}
    </ScrollView>
  );
};


const pickerSelectStyles = StyleSheet.create({
  inputIOS: {
    fontSize: 16,
    paddingVertical: 12,
    paddingHorizontal: 15,
    borderWidth: 1,
    borderColor: '#2291F2', 
    borderRadius: 30, 
    color: 'white',
    backgroundColor: '#1A2637', 
    marginBottom: 15,
    width: '100%',
    height: 50,
    justifyContent: 'center',
    alignItems: 'center',
    fontWeight: 'bold', 
  },
  inputAndroid: {
    fontSize: 16,
    paddingVertical: 12,
    paddingHorizontal: 15,
    borderWidth: 1,
    borderColor: '#2291F2', 
    borderRadius: 30, 
    color: 'white',
    backgroundColor: '#1A2637', 
    marginBottom: 15,
    width: '100%',
    height: 50,
    justifyContent: 'center',
    alignItems: 'center',
    fontWeight: 'bold', 
  },
});

const styles = StyleSheet.create({
  container: {
    padding: 20,
    backgroundColor: '#101526',
  },
  filterContainer: {
    marginBottom: 20,
  },
  filterLabel: {
    fontSize: 18,
    color: '#FFFFFF',
    marginBottom: 5,
  },
  loadingText: {
    fontSize: 18,
    color: '#2291F2',
    textAlign: 'center',
    marginTop: 20,
  },
  repoCard: {
    backgroundColor: '#1A2637',
    borderRadius: 15,
    padding: 20,
    marginBottom: 20,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 6,
    elevation: 5,
  },
  repoName: {
    fontSize: 20,
    color: '#FFFFFF',
    fontWeight: 'bold',
    marginBottom: 10,
  },
  repoDescription: {
    fontSize: 14,
    color: '#A9A9A9',
    lineHeight: 20,
  },
  noDescription: {
    fontSize: 14,
    color: '#A9A9A9',
    fontStyle: 'italic',
    marginTop: 5,
  },
});

export default ReposScreen;






