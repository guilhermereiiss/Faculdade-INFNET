import { AppBar, Toolbar, Typography, IconButton, InputBase } from '@mui/material';
import { Search as SearchIcon, Notifications, AccountCircle } from '@mui/icons-material';
import styles from './Header.module.css'; 

export default function Header() {
  return (
    <AppBar position="static" className={styles.barraApp}>
      <Toolbar className={styles.barraFerramentas}>
        <Typography variant="h6" component="div" className={styles.titulo}>
          INSTAGUI
        </Typography>
        <div className={styles.pesquisa}>
          <InputBase
            placeholder="Buscar..."
            inputProps={{ 'aria-label': 'search' }}
            startAdornment={<SearchIcon />}
            className={styles.entradaBase}
          />
        </div>
        <div className={styles.organizaOrdem}>
          <IconButton color="inherit">
            <Notifications />
          </IconButton>
          <IconButton color="inherit">
            <AccountCircle />
          </IconButton>
        </div>
      </Toolbar>
    </AppBar>
  );
}
