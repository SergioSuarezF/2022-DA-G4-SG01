import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

interface IThemeContext {
  dark: boolean;
  toggleDark?: () => void;
}

const defaultState = {
  dark: false,
};

const ThemeContext = React.createContext<IThemeContext>(defaultState);

const ThemeProvider: React.FC = ({ children }) => {
  const [dark, setDark] = React.useState(defaultState.dark);

  const toggleDark = () => {
    setDark(!dark);
  };

  return (
    <ThemeContext.Provider
      value={{
        dark,
        toggleDark,
      }}
    >
      {children}
    </ThemeContext.Provider>
  );
};

const ToggleDarkMode = () => {
  const { dark, toggleDark } = React.useContext(ThemeContext);
  const handleOnClick = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();
    toggleDark();
  };
  return (
    <>
      <h1>{dark ? "🌙" : "🌞"}</h1>
      <button onClick={handleOnClick}>Toggle dark mode</button>
    </>
  );
};

const App = () => {
  return (
    <ThemeProvider>
      <ToggleDarkMode />
    </ThemeProvider>
  );
};

ReactDOM.render(<App />, document.getElementById("root"));


