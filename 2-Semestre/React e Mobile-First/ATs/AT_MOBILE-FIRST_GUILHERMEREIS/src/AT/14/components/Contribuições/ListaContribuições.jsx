
import Contribuicao from './Contribuicao';
import styles from './ListaContribuições.module.css';

const ListaContribuições = ({ contribuições }) => {
  return (
    <div className={styles.lista}>
      {contribuições.map((contribuicao, index) => (
        <Contribuicao
          key={index}
          autor={contribuicao.autor}
          data={contribuicao.data}
          resposta={contribuicao.resposta}
          curtidas={contribuicao.curtidas}
        />
      ))}
    </div>
  );
};

export default ListaContribuições;
