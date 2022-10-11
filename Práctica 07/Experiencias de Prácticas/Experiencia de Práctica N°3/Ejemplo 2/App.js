/******************************************************
ARCHIVO : app.js
AUTOR : Joel Pinto
FECHA : 10/10/2022
DESCRIPCIÓN :  React Router
*******************************************************/
import React from 'react';
import Imagen from './logo.png';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
  useParams,
} from 'react-router-dom';

const App = () => (

  <Router>
    <img src={Imagen} />
    <Menu />
    <Contenido />
  </Router>
);

const Menu = () => (
  <ul>
    <Link to="/">Inicio</Link> |{" "}
    <Link to="/sistema">Sistema</Link> |{" "}
    <Link to="/info">Informacion</Link>
  </ul>
);

const Contenido = () => (
  <Routes>
    <Route exact path="/" element={<Inicio />} />
    <Route path="/sistema/*" element={<Sistema />} />
    <Route path="/info" element={<Info />} />
  </Routes>
);

const Inicio = () => (
  <><h1>Bienvenido!</h1></>
);

const Info = () => (
  <>
    <h1>Acerca de</h1>
    <p>React 6.4.2</p>
  </>
);

const Sistema = () => (
  <>
    <h1>Sistema de Matricula</h1>

    <Routes>
      <Route exact path="/" element={<Opciones />} />
      <Route path="/:id" element={<Opcion />} />
    </Routes>
  </>
);

const Opciones = () => (
  <>
    <ul>
      {Object.keys(OPCIONES).map(key => (
        <li key={key}>
          <Link to={`/sistema/${key}`}>{OPCIONES[key].opcion}</Link>
        </li>
      ))}
    </ul>
  </>
);

const Opcion = () => {
  const { id } = useParams();

  return (
    <>
      <h2>{OPCIONES[id].opcion}</h2>
      <p>
        <a href={OPCIONES[id].url}>Acceder</a>
      </p>
      <p>
        <Link to="/sistema">Regresar al sistema</Link>
      </p>
    </>
  );
};

const OPCIONES = {
  0: {
    opcion: 'Consolidado de Matricula',
    url: 'https://webapp.ucsm.edu.pe/',
  },
  1: {
    opcion: 'Consolidado de Notas',
    url: 'https://webapp.ucsm.edu.pe/',
  },
  2: {
    opcion: 'Horario',
    url: 'https://webapp.ucsm.edu.pe/',
  }
};

export default App;