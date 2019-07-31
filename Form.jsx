import React, {Component} from 'react';


export default class Form extends React.Component {
  render() {
    return (
      <div class = "form">
        <h1>Enter a Destination</h1>
        {/* action="http://localhost:5000/result" method="get */}
          <form onSubmit ={this.props.gettemperaturedata}> 
          Destination: <input type="text" name="place" />
          <button> Get Temperature </button>
          </form>
      </div>
    );
  }
}

