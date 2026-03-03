
import { View, Text, Button, FlatList } from 'react-native';

export default function Afinidade({ respostas, usuarios, alternarTela }) {
    const calcularAfinidade = (respostasUsuario) => {
        let afinidade = 0;
        Object.keys(respostas).forEach((item) => {
            if (respostas[item] === respostasUsuario[item]) {
                afinidade += 1;
            }
        });
        return afinidade;
    };

    const usuariosComAfinidade = usuarios
        .map((usuario) => ({
            ...usuario,
            afinidade: calcularAfinidade(usuario.respostas),
        }))
        .sort((a, b) => b.afinidade - a.afinidade);

    return (
        <View>
            <Text style={{ fontSize: 24, marginBottom: 10 }}>Usuários com Afinidade</Text>
            <FlatList
                data={usuariosComAfinidade}
                keyExtractor={(item) => item.nome}
                renderItem={({ item }) => (
                    <View style={{ marginBottom: 10 }}>
                        <Text>{item.nome} - Afinidade: {item.afinidade}</Text>
                    </View>
                )}
            />
            <Button title="Voltar" onPress={alternarTela} />
        </View>
    );
}
