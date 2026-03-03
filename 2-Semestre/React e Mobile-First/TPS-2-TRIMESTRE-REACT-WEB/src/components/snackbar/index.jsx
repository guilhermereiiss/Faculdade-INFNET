import { Snackbar } from '@mui/material';

const SnackbarComponent = ({ children, ...props }) => {
  return <Snackbar {...props}>{children}</Snackbar>;
};

export default SnackbarComponent;