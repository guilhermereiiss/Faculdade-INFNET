const BASE_URL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata';

export async function listarMoedas() {
  try {
    const response = await fetch(`${BASE_URL}/Moedas?$top=100&$format=json`);
    if (!response.ok) {
      throw new Error(`Erro ao buscar moedas: ${response.statusText}`);
    }
    const data = await response.json();
    return data.value;
  } catch (error) {
    console.error(error);
    return [];
  }
}

/**
 * Adquiri a cotação da moeda.
 * @param {string} moeda - codigoda moeda.
 * @param {string} dataCotacao - data na forma br.
 */
export async function obterCotacao(moeda, dataCotacao) {
  try {
    const url = `${BASE_URL}/CotacaoMoedaDia(moeda=@moeda,dataCotacao=@dataCotacao)?@moeda='${moeda}'&@dataCotacao='${dataCotacao}'&$top=1&$format=json`;
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Erro ao buscar cotação: ${response.statusText}`);
    }
    const data = await response.json();
    return data.value[0] || null;
  } catch (error) {
    console.error(error);
    return null;
  }
}
