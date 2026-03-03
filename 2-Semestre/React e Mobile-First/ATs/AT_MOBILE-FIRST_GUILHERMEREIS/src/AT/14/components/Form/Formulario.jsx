import styles from './Form.module.css';

const Form = ({ usuario }) => {
  return (
    <form className={styles.form}>
      <textarea
        placeholder="Escreva sua resposta..."
      />
      <div className={styles.footer}>
        <span>Usuário: {usuario}</span>
        <button type="submit">Enviar Resposta</button>
      </div>
    </form>
  );
};

export default Form;
