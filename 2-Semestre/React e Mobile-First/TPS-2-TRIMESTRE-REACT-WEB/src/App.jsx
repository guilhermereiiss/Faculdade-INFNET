import AppProvider from '../src/context/context'
import Routes from "./routes";

const App = () => {
  return (
    <AppProvider>
      <Routes />
    </AppProvider>
  );
};

export default App;
