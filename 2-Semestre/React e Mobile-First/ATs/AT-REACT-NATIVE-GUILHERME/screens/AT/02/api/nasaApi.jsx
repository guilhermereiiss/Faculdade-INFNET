
const BASE_URL = 'https://images-api.nasa.gov/search'; 

export const fetchAstroImages = async (astro, page = 1) => {
  try {
    const response = await fetch(`${BASE_URL}?q=${astro}&page=${page}`);
    const json = await response.json();
    const totalItems = json.collection.metadata.total_hits; 
    const items = json.collection.items; 
    return { items, totalItems };  
  } catch (error) {
    console.error('Erro ao buscar dados da NASA:', error);
    return { items: [], totalItems: 0 };
  }
};
