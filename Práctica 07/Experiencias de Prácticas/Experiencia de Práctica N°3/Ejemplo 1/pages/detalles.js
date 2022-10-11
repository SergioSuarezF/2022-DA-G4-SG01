/******************************************************
ARCHIVO : detalles.js
AUTOR : Joel Pinto
FECHA : 10/10/2022
DESCRIPCIÓN :  React Router
*******************************************************/
import { useParams } from "react-router-dom";
import Imagen from '../img/3.png';
const Detalles = () => {
  const { id } = useParams();
  return (
    <div>
      <p>Detalles del recibo:  #{id}</p>
      <img src={Imagen}/>
    </div>    
  );

};

export default Detalles;