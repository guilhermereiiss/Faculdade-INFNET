import { Box, Avatar, Typography } from '@mui/material';
import styles from './SugestaoAmigos.module.css';

const SugestaoAmigos = ({ sugestoes }) => {
  return (
    <Box className={styles.sugestoesContainer}>
      <Typography variant="h6" gutterBottom>
        Sugestões de Amizade
      </Typography>
      {sugestoes.map((sugestao) => (
        <Box key={sugestao.id} className={styles.sugestaoItem}>
          <Avatar src={sugestao.foto} alt={sugestao.nome} sx={{ mr: 2 }} />
          <Box>
            <Typography className={styles.nomeSugestao}>{sugestao.nome}</Typography>
            <Typography className={styles.amigosComum}>
              Amigo em comum: {sugestao.amigosEmComum}
            </Typography>
          </Box>
        </Box>
      ))}
    </Box>
  );
};

export default SugestaoAmigos;
