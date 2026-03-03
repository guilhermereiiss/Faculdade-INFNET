
export const adicionarFavorito = (id) => {
    const favoritos = JSON.parse(localStorage.getItem('favoritos')) || [];
    if (!favoritos.includes(id)) {
        favoritos.push(id);
        localStorage.setItem('favoritos', JSON.stringify(favoritos));
    }
};

export const removerFavorito = (id) => {
    const favoritos = JSON.parse(localStorage.getItem('favoritos')) || [];
    const novosFavoritos = favoritos.filter(favorito => favorito !== id);
    localStorage.setItem('favoritos', JSON.stringify(novosFavoritos));
};

export const obterFavoritos = () => {
    return JSON.parse(localStorage.getItem('favoritos')) || [];
};
