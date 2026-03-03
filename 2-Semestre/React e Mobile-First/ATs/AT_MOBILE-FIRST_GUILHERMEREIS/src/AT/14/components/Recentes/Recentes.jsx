import styles from './Recentes.module.css';

const TópicosRelacionados = ({ recentes, respondidos, curtidos }) => {
  return (
    <div className={styles.topicosRelacionados}>
      <section>
        <h4>Tópicos Recentes</h4>
        <ul>{recentes.map((topico, index) => <li key={index}>{topico}</li>)}</ul>
      </section>
      <section>
        <h4>Tópicos Mais Respondidos</h4>
        <ul>{respondidos.map((topico, index) => <li key={index}>{topico}</li>)}</ul>
      </section>
      <section>
        <h4>Tópicos Mais Curtidos</h4>
        <ul>{curtidos.map((topico, index) => <li key={index}>{topico}</li>)}</ul>
      </section>
    </div>
  );
};

export default TópicosRelacionados;