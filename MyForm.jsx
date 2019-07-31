import ReactDOM from 'react-dom';
import React, {Component} from 'react';
import './App.css';
import { forStatement } from '@babel/types';
import LineDemo from './LineDemo';
import { Line } from 'react-chartjs-2';


class MyForm extends React.Component {
  render() {
    return (
      <div class = "form">
        <h1>Enter a Destination</h1>
          <form action="http://localhost:5000/monthlytemperature/<variable>" method="get">
          Location: <input type="text"/>
          <input type="submit" value="Submit"
        />
      </form>
      </div>
    );
  }
}
ReactDOM.render(
  <MyForm/>,
  document.getElementById('root')
);
export default MyForm;
