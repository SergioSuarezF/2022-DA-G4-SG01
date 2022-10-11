//import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import React, { useState } from 'react';

/*
  function Ejemplo1(){
    const [inputText, setInputText] = useState('');
    const [valorAMostrar, setValorAMostrar] = useState(0);

    return (
        <div className="App">
            <input type="text" onChange={e=> setInputText(e.target.value)} />
            <button onClick={() => setValorAMostrar(inputText)}>Cambiar valor</button>
            <div>{valorAMostrar}</div>
        </div>
    );
}/*/


function Ejemplo2(){
  const [inputText, setInputText ] = useState('');

    return (
      <div className="App">
        <input type="text" onChange={e => setInputText(e.target.value)} />
        <div>{ inputText }</div>
      </div>
    );
}
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <Ejemplo2/>
);



// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
