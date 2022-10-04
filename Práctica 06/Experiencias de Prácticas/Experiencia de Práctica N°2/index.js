import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

function Bienvenida(props) {
  return <h1>Bienvenido a la zona de Usuario Registrados !</h1>;
}
 
function UsuarioAnonimo(props) {
  return <h1>Por favor, inicia sesión !</h1>;
}
 
function Saludo(props) {
  const isLoggedIn = props.isLoggedIn;
  if (isLoggedIn) {
    return <Bienvenida />;
  }
  return <UsuarioAnonimo />;
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
 <Saludo isLoggedIn ={true} />

);



// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
