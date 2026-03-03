
import { View, Text, Button } from 'react-native';

export default function Categoria({ categorias, selecionarCategoria }) {
  return (
    <View>
      <Text style={{ fontSize: 24, marginBottom: 10 }}>Categorias</Text>
      {categorias.map((categoria, index) => (
        <Button key={index} title={categoria} onPress={() => selecionarCategoria(categoria)} />
      ))}
    </View>
  );
}
