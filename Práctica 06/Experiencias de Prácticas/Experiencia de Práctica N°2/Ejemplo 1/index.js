import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

function formatName(user) {
  return user.firstName + ' ' + user.lastName;
}

const user1 = {
  firstName: 'Diego',
  lastName: 'Mendoza'
};

const user2 = {
  firstName: 'Sergio',
  lastName: 'Suarez'
};

const user3 = {
  firstName: 'Joel',
  lastName: 'Pinto'
};

const element = (
  <h1>
    Hello, {formatName(user1)}!<br></br>
    Hello, {formatName(user2)}!<br></br>
    Hello, {formatName(user3)}!<br></br>
  </h1>
);


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  element
);



// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
