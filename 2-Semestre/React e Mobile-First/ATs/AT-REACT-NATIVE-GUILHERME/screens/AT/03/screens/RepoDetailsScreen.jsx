import  { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity } from 'react-native';
import { getIssues } from '../api/githubApi';

const RepoDetailsScreen = ({ route }) => {
  const { repo } = route.params;
  const [issues, setIssues] = useState([]);

  useEffect(() => {
    const fetchIssues = async () => {
      const data = await getIssues(repo.owner.login, repo.name);
      setIssues(data);
    };

    fetchIssues();
  }, [repo]);

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <View style={styles.repoInfo}>
        <Text style={styles.title}>{repo.name}</Text>
        <Text style={styles.description}>{repo.description || "Sem descrição disponível"}</Text>
        <View style={styles.detailsContainer}>
          <Text style={styles.details}>Language: {repo.language}</Text>
          <Text style={styles.details}>Stars: {repo.stargazers_count}</Text>
          <Text style={styles.details}>Forks: {repo.forks_count}</Text>
          <Text style={styles.details}>Created on: {new Date(repo.created_at).toLocaleDateString()}</Text>
          <Text style={styles.details}>Last updated: {new Date(repo.updated_at).toLocaleDateString()}</Text>
        </View>
      </View>

      <View style={styles.issuesContainer}>
        <Text style={styles.issuesTitle}>Issues</Text>
        {issues.length === 0 ? (
          <Text style={styles.noIssues}>No issues found.</Text>
        ) : (
          issues.map((issue) => (
            <TouchableOpacity key={issue.id} style={styles.issueCard}>
              <Text style={styles.issueTitle}>{issue.title}</Text>
              <Text style={styles.issueDetails}>Author: {issue.user.login}</Text>
              <Text style={styles.issueDetails}>Comments: {issue.comments}</Text>
            </TouchableOpacity>
          ))
        )}
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    backgroundColor: '#101526',
    padding: 20,
  },
  repoInfo: {
    backgroundColor: '#1A2637',
    borderRadius: 10,
    padding: 15,
    marginBottom: 20,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 6,
    elevation: 5,
  },
  title: {
    fontSize: 28,
    color: '#FFFFFF',
    fontWeight: 'bold',
    marginBottom: 10,
  },
  description: {
    fontSize: 16,
    color: '#A9A9A9',
    marginBottom: 15,
  },
  detailsContainer: {
    marginTop: 10,
    borderTopWidth: 1,
    borderTopColor: '#A9A9A9',
    paddingTop: 10,
  },
  details: {
    fontSize: 16,
    color: '#FFFFFF',
    marginBottom: 8,
  },
  issuesContainer: {
    marginTop: 30,
  },
  issuesTitle: {
    fontSize: 22,
    color: '#FFFFFF',
    fontWeight: 'bold',
    marginBottom: 15,
  },
  noIssues: {
    fontSize: 16,
    color: '#A9A9A9',
    fontStyle: 'italic',
    textAlign: 'center',
  },
  issueCard: {
    backgroundColor: '#1A2637',
    borderRadius: 8,
    padding: 15,
    marginBottom: 15,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 6,
    elevation: 5,
  },
  issueTitle: {
    fontSize: 18,
    color: '#FFFFFF',
    fontWeight: 'bold',
    marginBottom: 5,
  },
  issueDetails: {
    fontSize: 14,
    color: '#A9A9A9',
  },
});

export default RepoDetailsScreen;
