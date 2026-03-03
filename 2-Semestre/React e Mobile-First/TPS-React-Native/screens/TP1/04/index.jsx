import { useState } from 'react';
import { Text, View, Image, Button } from 'react-native';

export default function App() {
  const images = [
    { title: 'Montanha', uri: 'https://png.pngtree.com/thumb_back/fh260/background/20230527/pngtree-8-best-free-mountain-background-images-4k-wallpapers-image_2670051.jpg' },
    { title: 'Praia', uri: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRlo5ESDoEMxeApJV9_VzlusmEjeVkCE-73g&s' },
    { title: 'Floresta', uri: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwwd3vzhrxgIWHLkQYzm25P-F9ceOP7_c1IA&s' },
  ];

  const [currentImage, setCurrentImage] = useState(images[0]);

  const changeImage = () => {
    const randomIndex = Math.floor(Math.random() * images.length);
    setCurrentImage(images[randomIndex]);
  };

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Image
        source={{ uri: currentImage.uri }}
        style={{ width: 300, height: 200, marginBottom: 20 }}
      />
      <Text style={{ fontSize: 24, marginBottom: 20 }}>{currentImage.title}</Text>
      <Button title="Alterar Imagem" onPress={changeImage} />
    </View>
  );
}
