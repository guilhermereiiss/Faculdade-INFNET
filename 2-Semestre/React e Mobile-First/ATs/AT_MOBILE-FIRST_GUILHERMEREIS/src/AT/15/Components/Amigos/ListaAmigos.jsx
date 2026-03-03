import { Box, Avatar, Typography } from '@mui/material';
import styles from './ListaAmigos.module.css'; 

const ListaAmigos = ({ amigos }) => {
  return (
    <Box className={styles.listaContainer}>
      <Typography variant="h6" gutterBottom>
        Amigos
      </Typography>
      {amigos.map((amigo) => (
        <Box key={amigo.id} className={styles.amigoItem}>
          <Avatar src={amigo.foto} alt={amigo.nome} sx={{ mr: 2 }} />
          <Box>
            <Typography className={styles.nomeAmigo}>{amigo.nome}</Typography>
            <Typography className={styles.amigosComum}>
              {amigo.amigosEmComum} amigos em comum
            </Typography>
          </Box>
        </Box>
      ))}
    </Box>
  );
};

export default ListaAmigos;
