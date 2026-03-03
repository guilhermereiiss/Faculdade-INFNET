
import { Button } from '@mui/material';

const ButtonComponent = ({ children, variant = "contained", size = "large", className = "", ...props }) => {
  return (
    <Button 
      className={`general-button ${className}`}
      variant={variant}
      size={size}
      {...props}
    >
      {children}
    </Button>
  );
};

export default ButtonComponent;
