import { Typography } from '@mui/material';

const TextComponent = ({ children, ...props }) => {
  return <Typography {...props}>{children}</Typography>;
};

export default TextComponent;