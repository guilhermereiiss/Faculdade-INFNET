import { Fab } from '@mui/material';

const FabComponent = ({ children, ...props }) => {
  return <Fab {...props}>{children}</Fab>;
};

export default FabComponent;