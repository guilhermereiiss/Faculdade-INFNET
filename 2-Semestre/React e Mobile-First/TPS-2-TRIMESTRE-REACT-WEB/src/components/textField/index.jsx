import { TextField } from '@mui/material';

const TextFieldComponent = ({ variant = "outlined", className = "", ...props }) => {
  return (
    <TextField
      className={`general-textfield ${className}`}
      variant={variant}
      {...props}
    />
  );
};

export default TextFieldComponent;