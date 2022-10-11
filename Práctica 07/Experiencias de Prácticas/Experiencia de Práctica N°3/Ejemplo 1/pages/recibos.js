/******************************************************
ARCHIVO : recibos.js
AUTOR : Joel Pinto
FECHA : 10/10/2022
DESCRIPCIÓN :  React Router
*******************************************************/
import { Outlet } from "react-router-dom";
import { Link } from "react-router-dom";
const Recibos = () => {
  return (
    <main style={{ padding: "1rem 0" }}>
      <p>Recibos</p>
      <li><Link to="1">Recibo #1</Link></li>
      <li><Link to="2">Recibo #2</Link></li>
      <li><Link to="3">Recibo #3</Link></li>
      <li><Link to="100">Recibo #100</Link></li>
      <li><Link to="5246">Recibo #5246</Link></li>
      <Outlet/>
    </main>
  );
};
export default Recibos;