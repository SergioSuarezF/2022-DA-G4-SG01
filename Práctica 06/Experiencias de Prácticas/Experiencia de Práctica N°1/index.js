import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

function tick() {
  const elemento = (
    <div>
      <h1> Hola mundo!!! </h1>
      <h2> Hora:{new Date().toLocaleTimeString} </h2>
    </div>
  );
  root.render(elemento)
}

setInterval(tick,1000)

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)

reportWebVitals();

