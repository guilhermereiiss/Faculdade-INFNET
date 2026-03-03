import styles from './Tópico.module.css';

const TópicoPrincipal = ({ titulo, subtitulo, descricao, autor, data, curtidas, respostas }) => {
  return (
    <section className={styles.topico}>
      <h2>{titulo}</h2>
      <h3>{subtitulo}</h3>
      <p>{descricao}</p>
      <div className={styles.info}>
        <span>Por: {autor}</span> | <span>Data: {data}</span>
      </div>
      <div className={styles.marcadores}>
        <span>👍 {curtidas} curtidas</span> | <span>💬 {respostas} respostas</span>
      </div>
    </section>
  );
};

export default TópicoPrincipal;