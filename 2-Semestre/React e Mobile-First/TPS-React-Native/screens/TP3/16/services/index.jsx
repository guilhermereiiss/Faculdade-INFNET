import axios from 'axios';

const API_URL = 'https://servicodados.ibge.gov.br/api/v3/noticias';

export const fetchNews = async (params = {}) => {
    try {
        const response = await axios.get(API_URL, { params });
        return response.data.items;
    } catch (error) {
        console.error("Erro ao buscar notícias:", error);
        return [];
    }
};

