import ReactDOM from 'react-dom';
import React, {Component} from 'react';
import './App.css';
import { forStatement } from '@babel/types';
import LineDemo from './LineDemo';
import { Line } from 'react-chartjs-2';


class App extends React.Component {
  render() {
    return (
      <div class = "form">
        <h1>Enter a Destination</h1>
          <form action="http://localhost:5000/monthlytemperature/Albania" method="get">
          Destination: <input type="text"/>
          <input type="submit" value="Submit"
        />
      </form>
      </div>
    );
  }
}
ReactDOM.render(
  <App/>,
  document.getElementById('root')
);
export default App;
