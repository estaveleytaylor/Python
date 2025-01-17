import React from 'react';
import { render } from 'react-dom';
import LineDemo from './LineDemo';
import App from './App';

const styles = {
  fontFamily: 'sans-serif',
  textAlign: 'center',
};

const App = () => (
  <div style={styles}>
    <LineDemo/>
  </div>
);

render(<App />, document.getElementById('root'));
