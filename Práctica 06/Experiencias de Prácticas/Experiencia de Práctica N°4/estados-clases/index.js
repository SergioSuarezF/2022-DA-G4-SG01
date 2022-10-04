/******************************************************
ARCHIVO : index.js
AUTOR : Joel Pinto
FECHA : 03/10/2022
DESCRIPCIÓN :  USO DE ESTADOS CON CLASES
*******************************************************/
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

class Contador extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      cont: 0,
    }
  };

  mas = () => {
    this.setState({
      cont: this.state.cont + 1
    });
    console.log('Cont: ', this.state.cont);
  };

  menos = () => {
    this.setState({
      cont: this.state.cont - 1
    });
    console.log('Cont: ', this.state.cont);
  };

  restart = () => {
    this.setState({
      cont: this.state.cont = 0
    });
    console.log('Cont: ', this.state.cont);
  };

  render() {
    return (
      <div>
        <header>
          <h1>Contador: {this.state.cont}</h1>
          <button onClick={this.mas}>+</button>
          <button onClick={this.menos}>-</button>
          <button onClick={this.restart}>Reiniciar</button>
        </header>
      </div>
    );
  }

}
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Contador />);