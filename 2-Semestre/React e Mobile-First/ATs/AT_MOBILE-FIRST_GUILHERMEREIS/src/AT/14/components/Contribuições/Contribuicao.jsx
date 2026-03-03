
import styles from './Contribuicao.module.css';

const Contribuição = ({ autor, data, resposta, curtidas }) => {
  return (
    <div className={styles.contribuicao}>
      <p>{resposta}</p>
      <div className={styles.info}>
        <span>Por: {autor}</span> | <span>Data: {data}</span> | <span>👍 {curtidas} curtidas</span>
      </div>
    </div>
  );
};

export default Contribuição;
