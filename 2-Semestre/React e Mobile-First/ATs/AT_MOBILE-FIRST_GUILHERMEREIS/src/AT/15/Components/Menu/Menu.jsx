import { BottomNavigation, BottomNavigationAction, Paper } from '@mui/material';
import { Home, People, Message, Notifications } from '@mui/icons-material';
import { useState } from 'react';
import styles from './Menu.module.css'; 

export default function Menu() {
  const [valor, setValor] = useState(0);

  return (
    <Paper className={styles.menuContainer}>
      <BottomNavigation
        value={valor}
        onChange={(event, novoValor) => {
          setValor(novoValor);
        }}
        className={styles.navegacaoInferior}
      >
        <BottomNavigationAction label="Feed" icon={<Home />} />
        <BottomNavigationAction label="Amigos" icon={<People />} />
        <BottomNavigationAction label="Mensagens" icon={<Message />} />
        <BottomNavigationAction label="Notificações" icon={<Notifications />} />
      </BottomNavigation>
    </Paper>
  );
}



