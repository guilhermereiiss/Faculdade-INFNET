import styles from "./Comentarios.module.css";

const Comentarios = ({ comentarios }) => {
  return (
    <section className={styles.container}>
      <h3>Comentários</h3>
      {comentarios.map((comentario, index) => (
        <div key={index} className={styles.comentario}>
          <p>
            <span>{comentario.nomeUsuario}</span>
            <span className={styles.data}> - {comentario.data}</span>
          </p>
          <p>{comentario.mensagem} <span className={styles.nota}>Nota: {comentario.nota}</span></p>
        </div>
      ))}
    </section>
  );
};

export default Comentarios;
