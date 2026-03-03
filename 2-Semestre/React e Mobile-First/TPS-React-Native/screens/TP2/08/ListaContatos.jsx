
import { FlatList } from 'react-native';
import ContatoItem from './ContatoItem.jsx';

const ListaContatos = ({ dados }) => {
  return (
    <FlatList
      data={dados}
      keyExtractor={(item) => item.id.toString()}
      renderItem={({ item }) => (
        <ContatoItem 
          avatar={item.avatar} 
          nome={item.nome} 
          endereco={item.endereco} 
          numero={item.numero} 
        />
      )}
    />
  );
};

export default ListaContatos;
