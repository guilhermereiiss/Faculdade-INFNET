import { Box } from '@mui/material';
import Post from './Post';
import styles from './Feed.module.css'; 

const postsData = [
  {
    id: 1,
    autor: "João Silva",
    avatar: "https://placehold.co/150",
    image: "https://placehold.co/600x400",
    texto: "Hoje foi um dia incrível na praia!",
    date: "2024-09-23",
    likes: 23,
    compartilhar: 5,
    comentarios: [
      { id: 1, autor: "Maria", texto: "Lindo lugar!" },
      { id: 2, autor: "Pedro", texto: "Queria estar lá!" }
    ]
  },
  {
    id: 2,
    autor: "Lucas Fernandes",
    avatar: "https://placehold.co/150",
    image: "https://placehold.co/600x400",
    texto: "Hoje foi demitido",
    date: "2024-09-23",
    likes: 5000,
    compartilhar: 753,
    comentarios: [
      { id: 1, autor: "Alexandre", texto: "Que pena mano, sucesso na caminhada!" },
      { id: 2, autor: "Guilherme", texto: "Quem não mandou fazer o M de Marçal" }
    ]
  },
  {
    id: 3,
    autor: "Alexandre Gonçalves",
    avatar: "https://placehold.co/150",
    image: "https://placehold.co/600x400",
    texto: "Hoje bati minhas metas de vendas escalaveis",
    date: "2024-09-23",
    likes: 17432,
    compartilhar:2324,
    comentarios: [
      { id: 1, autor: "Lucas", texto: "Parabens amigo!!" },
      { id: 2, autor: "Guilherme", texto: "Fez o M de Marçal e deu certo kkkkkkkkkkkk" }
    ]
  },
];

export default function Feed() {
  return (
    <Box className={styles.feedContainer}>
      {postsData.map((post) => (
        <Box key={post.id} className={styles.postWrapper}>
          <Post post={post} />
        </Box>
      ))}
    </Box>
  );
}
