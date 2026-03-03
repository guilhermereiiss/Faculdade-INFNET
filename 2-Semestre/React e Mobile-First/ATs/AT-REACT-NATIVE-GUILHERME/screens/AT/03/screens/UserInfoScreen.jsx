import { useEffect, useState } from 'react';
import { View, Text, Image, StyleSheet, ScrollView, TouchableOpacity } from 'react-native';
import { getUserInfo } from '../api/githubApi';

const UserInfoScreen = ({ route, navigation }) => {
  const { token } = route.params;
  const [userInfo, setUserInfo] = useState(null);

  useEffect(() => {
    const fetchUserInfo = async () => {
      const data = await getUserInfo(token);
      setUserInfo(data);
    };

    fetchUserInfo();
  }, [token]);

  if (!userInfo) {
    return <Text style={styles.loadingText}>Carregando...</Text>;
  }

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Image
        source={{ uri: userInfo.avatar_url }}
        style={styles.avatar}
      />
      <Text style={styles.name}>{userInfo.name}</Text>
      <Text style={styles.login}>@{userInfo.login}</Text>

      <View style={styles.statsContainer}>
        <View style={styles.statsCard}>
          <Text style={styles.statsLabel}>Repos</Text>
          <Text style={styles.statsValue}>{userInfo.public_repos}</Text>
        </View>
        <View style={styles.statsCard}>
          <Text style={styles.statsLabel}>Following</Text>
          <Text style={styles.statsValue}>{userInfo.following}</Text>
        </View>
        <View style={styles.statsCard}>
          <Text style={styles.statsLabel}>Followers</Text>
          <Text style={styles.statsValue}>{userInfo.followers}</Text>
        </View>
      </View>

      <View style={styles.buttonsContainer}>
        <TouchableOpacity
          style={styles.button}
          onPress={() => navigation.navigate('Repos', { token })} 
        >
          <Text style={styles.buttonText}>Repositórios</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={styles.button}
          onPress={() => navigation.navigate('Issues', { token })} 
        >
          <Text style={styles.buttonText}>Issues</Text>
        </TouchableOpacity>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    backgroundColor: '#101526',
    padding: 20,
  },
  avatar: {
    width: 120,
    height: 120,
    borderRadius: 60,
    borderWidth: 2,
    borderColor: '#1A6DD9',
    marginBottom: 20,
  },
  name: {
    fontSize: 24,
    color: '#FFFF',
    fontWeight: 'bold',
    marginBottom: 10,
  },
  login: {
    fontSize: 18,
    color: '#2291F2',
    marginBottom: 20,
  },
  statsContainer: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    width: '100%',
    marginTop: 20,
  },
  statsCard: {
    backgroundColor: '#1A2637', 
    paddingVertical: 20,
    paddingHorizontal: 30,
    borderRadius: 10,
    alignItems: 'center',
    width: '28%',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.8,
    shadowRadius: 5,
    elevation: 5, 
  },
  statsLabel: {
    fontSize: 16,
    color: '#AAAAAA', 
  },
  statsValue: {
    fontSize: 18,
    color: '#2291F2',
    fontWeight: 'bold',
  },
  loadingText: {
    fontSize: 18,
    color: '#2291F2',
    textAlign: 'center',
    marginTop: 20,
  },
  buttonsContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    width: '100%',
    marginTop: 30,
  },
  button: {
    backgroundColor: '#1A6DD9',
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 5,
    width: '45%',
    alignItems: 'center',
  },
  buttonText: {
    color: '#FFFF',
    fontSize: 18,
    fontWeight: 'bold',
  },
});

export default UserInfoScreen;
