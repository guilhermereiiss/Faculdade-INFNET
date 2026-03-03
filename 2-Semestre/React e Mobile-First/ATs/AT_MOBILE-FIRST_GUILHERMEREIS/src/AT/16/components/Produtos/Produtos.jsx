import styles from "./Produtos.module.css";

const ProdutosRelacionados = ({ produtos }) => {
  return (
    <section className={styles.container}>
      <h3>Produtos Relacionados</h3>
      {produtos.map((produto, index) => (
        <div key={index} className={styles.produtoCard}>
          <img src={produto.imagem} alt={produto.nome} />
          <h4>{produto.nome}</h4>
          <p>
            Preço: <span>R${produto.preco.toFixed(2)}</span>
          </p>
          <button className={styles.button}>Adicionar ao carrinho</button>
        </div>
      ))}
    </section>
  );
};

export default ProdutosRelacionados;
