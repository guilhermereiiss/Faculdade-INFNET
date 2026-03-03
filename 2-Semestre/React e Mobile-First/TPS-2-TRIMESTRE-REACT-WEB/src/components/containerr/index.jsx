
import { Container } from '@mui/material';

const ContainerComponent = ({ children, ...props }) => {
  return <Container {...props}>{children}</Container>;
};

export default ContainerComponent;
