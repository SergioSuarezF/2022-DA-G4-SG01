/******************************************************
ARCHIVO : App.js
AUTOR : Joel Pinto
FECHA : 10/10/2022
DESCRIPCIÓN :  React Router
*******************************************************/
import { Outlet, Link } from "react-router-dom";

function App() {
  return (
    <div>
      <h1>Dashboard</h1>
      <nav>
        <Link to="/clientes">Clientes</Link> |{" "}
        <Link to="/cuentas">Cuentas</Link> |{" "}
        <Link to="/recibos">Recibos</Link>
      </nav>
      <Outlet />
    </div>
  );
}

export default App;
