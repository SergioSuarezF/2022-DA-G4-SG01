/******************************************************
ARCHIVO : recibos.js
AUTOR : Joel Pinto
FECHA : 10/10/2022
DESCRIPCIÓN :  React Router
*******************************************************/
import { Outlet } from "react-router-dom";
const Recibos = () => {
  return (
    <main style={{ padding: "1rem 0" }}>
      <p>Recibos</p>
      <Outlet/>
    </main>
  );
};
export default Recibos;