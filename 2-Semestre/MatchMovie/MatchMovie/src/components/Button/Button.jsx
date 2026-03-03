
import styles from './Botao.module.css'; 

const Botao = ({ label, onClick, tipo = 'button', estilo }) => {
  return (
    <button className={`${styles.botao} ${styles[estilo]}`} type={tipo} onClick={onClick}>
      {label}
    </button>
  );
};

export default Botao;
