import { useState } from 'react';
import { View, Text, Button, FlatList } from 'react-native';
import Preferencia from './Preferencia.jsx';
import Afinidade from './Afinidade.jsx';

export default function App() {
    const [pagina, setPagina] = useState('preferencia');
    const [respostas, setRespostas] = useState({});

    const itens = ["Filme A", "Música B", "Jogo C", "Filme D", "Música E"];

    const usuarios = [
        { nome: "Usuário 1", respostas: { "Filme A": true, "Música B": false, "Jogo C": true, "Filme D": true, "Música E": false } },
        { nome: "Usuário 2", respostas: { "Filme A": false, "Música B": true, "Jogo C": true, "Filme D": false, "Música E": true } },
        { nome: "Usuário 3", respostas: { "Filme A": true, "Música B": false, "Jogo C": true, "Filme D": true, "Música E": true } },
    ];
    const alternarTela = () => {
        setPagina(pagina === 'preferencia' ? 'afinidade' : 'preferencia');
    };

    return (
        <View style={{ flex: 1, padding: 20 }}>
            {pagina === 'preferencia' ? (
                <Preferencia itens={itens} respostas={respostas} setRespostas={setRespostas} alternarTela={alternarTela} />
            ) : (
                <Afinidade respostas={respostas} usuarios={usuarios} alternarTela={alternarTela} />
            )}
        </View>
    );
}
