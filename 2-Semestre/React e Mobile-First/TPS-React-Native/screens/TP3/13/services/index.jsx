export const fetchProposiçao = async () => {
  try {
    const response = await fetch(
      "https://dadosabertos.camara.leg.br/api/v2/proposicoes"
    );
    const data = await response.json();
    return data.dados || [];
  } catch (error) {
    console.error("Erro ao buscar proposições:", error);
    return [];
  }
};
