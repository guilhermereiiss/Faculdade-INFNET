import { useState } from 'react';
import { Tab, Tabs, Box } from '@mui/material';

const TabsComponent = ({ tabs }) => {
  const [value, setValue] = useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <Box>
      <Tabs value={value} onChange={handleChange} aria-label="tabs component">
        {tabs.map((tab, index) => (
          <Tab key={index} label={tab.label} />
        ))}
      </Tabs>

      {tabs.map((tab, index) => (
        <div role="tabpanel" hidden={value !== index} key={index}>
          {value === index && <Box p={3}>{tab.content}</Box>}
        </div>
      ))}
    </Box>
  );
};

export default TabsComponent;
