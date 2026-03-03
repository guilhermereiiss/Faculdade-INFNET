import { Box, Typography } from '@mui/material';

const listaComentarios = ({ comentarios }) => {
  return (
    <Box sx={{ mt: 2 }}>
      {comentarios.map((comentario) => (
        <Box key={comentario.id} sx={{ mb: 1 }}>
          <Typography variant="body2" component="span" fontWeight="bold">
            {comentario.autor}:
          </Typography>
          <Typography variant="body2" component="span" sx={{ ml: 1 }}>
            {comentario.texto}
          </Typography>
        </Box>
      ))}
    </Box>
  );
};

export default listaComentarios;