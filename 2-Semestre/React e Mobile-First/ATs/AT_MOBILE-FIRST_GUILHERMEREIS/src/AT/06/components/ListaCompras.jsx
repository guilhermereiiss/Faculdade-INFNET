
import styles from "./ListaCompras.module.css";

const ListaCompras = ({ itens }) => {
    const calculoDasCompras = () => {
        return itens.reduce(
            (total, item) => total + item.valorUnitario * item.quantidade,
            0
        );
    };

    return (
        <div className={styles.container}>
            <h1 className={styles.titulo}>Lista de Compras - AT</h1>
            <ul className={styles.lista}>
                {itens.map((item, index) => (
                    <li key={index} className={styles.item}>
                        <div className={styles.detalhesItem}>
                            <p className={styles.nome}>{item.nome}</p>
                            <p>R$ {item.valorUnitario.toFixed(2)}</p>
                            <p>Qtd: {item.quantidade}</p>
                            <p>Total: R$ {(item.valorUnitario * item.quantidade).toFixed(2)}</p>
                        </div>
                    </li>
                ))}
            </ul>
            <div className={styles.totalCompra}>
                <p><strong>Total da Compra: R$ {calculoDasCompras().toFixed(2)}</strong></p>
            </div>
        </div>
    );
};

export default ListaCompras;
