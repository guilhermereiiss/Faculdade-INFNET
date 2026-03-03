const BASE_URL = "https://openlibrary.org";

export const searchBooks = async (query) => {
  try {
    const response = await fetch(`${BASE_URL}/search.json?q=${query}`);
    return await response.json();
  } catch (error) {
    console.error("Error books:", error);
  }
};

export const fetchBookDetails = async (key) => {
  try {
    const response = await fetch(`${BASE_URL}${key}.json`);
    return await response.json();
  } catch (error) {
    console.error("Erro detalhes book", error);
  }
};
