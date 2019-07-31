import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Form from './Form';
import { Line } from 'react-chartjs-2';
import {Bar} from 'react-chartjs-2';

class App extends React.Component {

  constructor() {
    super();
  }
  state = {
    temperatureData: []
  }

  gettemperaturedata = async (e) => {
    e.preventDefault();
    const place = e.target.elements.place.value;

    const api_call = await fetch(`http://localhost:5000/monthlytemperature/${place}`);
    const data = await api_call.json();
    //  .then(results => {
    //     return results.json();
    //   })
    //   .then(data => {
        this.setState({
          temperatureData: data.Monthly.MonthlyTemperature
        })
      
  }


  render() {
    console.log(this.state.temperatureData)
    const data = {
      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
      datasets: [
        {
          label: 'Temperature',
          fill: false,
          lineTension: 0.1,
          backgroundColor: 'rgba(75,192,192,0.4)',
          borderColor: 'rgba(75,192,192,1)',
          borderCapStyle: 'butt',
          borderDash: [],
          borderDashOffset: 0.0,
          borderJoinStyle: 'miter',
          pointBorderColor: 'rgba(75,192,192,1)',
          pointBackgroundColor: '#fff',
          pointBorderWidth: 1,
          pointHoverRadius: 5,
          pointHoverBackgroundColor: 'rgba(75,192,192,1)',
          pointHoverBorderColor: 'rgba(220,220,220,1)',
          pointHoverBorderWidth: 2,
          pointRadius: 1,
          pointHitRadius: 10,
          data: this.state.temperatureData
        }
      ]
    };
    return (
     
      <div>
        <div>
          <Form gettemperaturedata={this.gettemperaturedata} />
          {/* <Form getprecipdata={this.getprecipdata} /> */}
        </div>
        <h2>Monthly Average Temperature</h2>
        <Line ref="chart" data={data} />
      </div>
    );

  
    
  }
  
  componentDidMount() {
    const { datasets } = this.refs.chart.chartInstance.data
    // console.log(datasets[0].data);
  }

}


export default App;
