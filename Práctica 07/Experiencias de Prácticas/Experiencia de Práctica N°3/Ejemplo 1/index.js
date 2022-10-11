/******************************************************
ARCHIVO : index.js
AUTOR : Joel Pinto
FECHA : 10/10/2022
DESCRIPCIÓN :  React Router
*******************************************************/
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import Clientes from "./pages/clientes";
import Cuentas from "./pages/cuentas";
import Recibos from "./pages/recibos";
import Detalles from './pages/detalles';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />}>          
          <Route path="clientes" element={<Clientes />} />
          <Route path="cuentas" element={<Cuentas />} />
          <Route path="recibos" element={<Recibos />}>
            <Route path=":id" element={<Detalles />} />
          </Route>
        </Route>
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);