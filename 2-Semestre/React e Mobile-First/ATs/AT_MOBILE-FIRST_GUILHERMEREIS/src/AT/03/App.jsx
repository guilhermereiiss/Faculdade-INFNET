import styles from "./styles.module.css"; 
import { useState } from 'react';

export default function App() { 
    const [images, setImages] = useState([1, 2, 3, 4, 5]);

    const addImagem = () => {
        setImages([...images, images.length + 1]);
    };

    const apagarImagem = () => {
        if (images.length > 0) {
            setImages(images.slice(0, -1));
        }
    };

    return (
        <div className={styles.container}>
            <div className={styles.controle}>
                <button onClick={addImagem}>Adicionar</button>
                <span>{images.length}</span>
                <button onClick={apagarImagem}>Remover</button>
            </div>
            <div className={styles.gallery}>
                {images.map((img, index) => (
                    <div key={index} className={styles.image}>
                        <span>100 x 100</span>
                    </div>
                ))}
            </div>
        </div>
    );
}
