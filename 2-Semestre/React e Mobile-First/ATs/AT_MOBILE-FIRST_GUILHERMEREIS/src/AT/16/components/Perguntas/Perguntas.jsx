import styles from "./Perguntas.module.css";

const Perguntas = ({ perguntas }) => {
  return (
    <section className={styles.container}>
      <h3>Perguntas</h3>
      {perguntas.map((pergunta, index) => (
        <div key={index} className={styles.pergunta}>
          <p><span className={styles.nomeUsuario}>{pergunta.nomeUsuario}</span> - <span className={styles.data}>{pergunta.data}</span></p>
          <p className={styles.duvida}>Dúvida: {pergunta.duvida}</p>
          <p className={styles.resposta}>Resposta: {pergunta.resposta}</p>
        </div>
      ))}
    </section>
  );
};

export default Perguntas;
