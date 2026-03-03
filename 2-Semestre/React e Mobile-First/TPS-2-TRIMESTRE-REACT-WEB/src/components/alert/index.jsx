
import { Alert } from '@mui/material';

const AlertComponent = ({ children, ...props }) => {
  return <Alert {...props}>{children}</Alert>;
};

export default AlertComponent;
