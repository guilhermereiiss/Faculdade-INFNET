import { Container, Typography, Table, TableBody, TableCell, TableHead, TableRow, Paper } from '@mui/material';

const Compras = ({ itens }) => {
  const calcularTotal = () => {
    return itens.reduce((acc, item) => acc + item.quantidade * item.valorUnitario, 0).toFixed(2);
  };

  return (
    <Container sx={{ padding: '16px', maxWidth: { xs: '100%', md: '80%' } }}>
      <Typography variant="h4" align="center" gutterBottom>
        Lista de Itens de Compra
      </Typography>

      <Paper elevation={3} sx={{ padding: '16px', marginBottom: '16px', width: '100%', overflowX: 'auto' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Nome</TableCell>
              <TableCell align="right">Valor Unitário</TableCell>
              <TableCell align="right">Quantidade</TableCell>
              <TableCell align="right">Valor Total do Item</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {itens.map((item) => (
              <TableRow key={item.nome}>
                <TableCell>{item.nome}</TableCell>
                <TableCell align="right">R$ {item.valorUnitario.toFixed(2)}</TableCell>
                <TableCell align="right">{item.quantidade}</TableCell>
                <TableCell align="right">R$ {(item.valorUnitario * item.quantidade).toFixed(2)}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </Paper>

      <Typography variant="h6" align="right">
        Valor Total das Compras é: R$ {calcularTotal()}
      </Typography>
    </Container>
  );
};

export default Compras;
