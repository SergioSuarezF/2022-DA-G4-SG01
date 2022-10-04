import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

function START(){ 

  const objStyle={ 
    fontSize:"50px",
    color:"skyblue", 
    textAlign:'center' 
  } 
  
  return ( 
    <div> 
      <h1 style={objStyle}>Die Startelf</h1> 
      <h2 style={{color:"Red",textAlign:'center'}}>Des FC Bayern München</h2> 
      <h1> Mit der Nummer Eins und Unsere Kapitän: Manuel Neuer </h1> 
    </div> 
  ); 

} 
  
const root= ReactDOM.createRoot(document.getElementById('root')); 
root.render(<START/>);



