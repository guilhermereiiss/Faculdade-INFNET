import styles from "./Detalhes.module.css";

const DetalhesProduto = ({ produto }) => {
    return (
        <section className={styles.container}>
            <div className={styles.imagemOrg}>
                <img className={styles.imagem} src={produto.imagem} alt={produto.nome} />
            </div>
            <div className={styles.ogrRestante}>
                <h2 className={styles.titulo}>{produto.nome}</h2>
                <p className={styles.descricao}>{produto.descricao}</p>
                <p className={styles.preco}>Preço: R${produto.preco.toFixed(2)}</p>
                <p className={styles.nota}>Nota: {produto.nota} / 5</p>
                <button className={styles.botaoAdicionar}>Adicionar ao Carrinho</button>
            </div>
        </section>
    );
};

export default DetalhesProduto;
