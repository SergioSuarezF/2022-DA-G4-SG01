
//import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { useState, useEffect } from "react";


/*function Contadores() {
  const [count1, setCount1] = useState(0);
  const [count2, setCount2] = useState(0);
  const [count3, setCount3] = useState(0);

  useEffect(() => {
    console.log("count2 changed!");
  }, [count2]);

  return (
    <div>
      {count1} {count2} {count3}
      <br />
      <button onClick={() => setCount1(count1 + 1)}>Incrementar contador 1</button>
      <button onClick={() => setCount2(count2 + 1)}>Incrementar contador 2</button>
      <button onClick={() => setCount3(count3 + 1)}>Incrementar contador 3</button>
    </div>
  );
}/*/


function Cambio() {

  const [texto, setTexto] = useState("")

  useEffect(() => {document.title = texto}, [texto])

  function cambiar(e) {
    setTexto(e.target.value)
  }

  return (
    <div>
      <p><input type="text" onChange={cambiar} /></p>
      <p>{texto}</p>
    </div>
  );
}
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
 <Cambio/>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
