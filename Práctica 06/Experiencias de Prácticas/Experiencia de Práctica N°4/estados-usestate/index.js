/******************************************************
ARCHIVO : index.js
AUTOR : Joel Pinto
FECHA : 03/10/2022
DESCRIPCIÓN :  USO DE ESTADOS CON USESTATE
*******************************************************/
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import { useState } from 'react';

function Contador() {
  const [cont, setCont] = useState(0);

  const mas = () => {
    setCont(cont + 1);
    console.log('Cont: ', cont);
  };

  const menos = () => {
    setCont(cont - 1);
    console.log('Cont: ', cont);
  };

  const restart = () => {
    setCont(cont = 1);
    console.log('Cont: ', cont);
  };

  return (
    <div>
      <header>
        <h1>Contador: {cont}</h1>
        <button onClick={mas}>+</button>
        <button onClick={menos}>-</button>
        <button onClick={restart}>Reiniciar</button>
      </header>
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Contador />);