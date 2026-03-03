
const API_URL = 'https://api.github.com';

export const getUserInfo = async (token) => {
  const response = await fetch(`${API_URL}/user`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return await response.json();
};

export const getRepos = async (token, page = 1) => {
  const response = await fetch(`${API_URL}/user/repos?page=${page}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return await response.json();
};
export const getIssues = async (owner, repoName) => {
    try {
      const response = await fetch(`https://api.github.com/repos/${owner}/${repoName}/issues`);
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error fetching issues:', error);
      return [];
    }
  };
  