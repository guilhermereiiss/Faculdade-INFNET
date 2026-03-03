import styles from "./Vendedor.module.css";

const Vendedor = ({ vendedor }) => {
  return (
    <section className={styles.container}>
      <h3>Informações do Vendedor</h3>
      <p>Nome: <span>{vendedor.nome}</span></p>
      <p>Email: <span>{vendedor.email}</span></p>
      <p>Telefone: <span>{vendedor.telefone}</span></p>
      <p>Nota: <span className={styles.nota}>{vendedor.nota}</span> / 5</p>
    </section>
  );
};

export default Vendedor;
