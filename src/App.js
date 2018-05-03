import React, { Component } from 'react';
import DATA from './data-huon.json';
import './App.css';
import Button from './components/common/button/button'

const ButtonConfig = {
  title: "Get Quote Info",
}

class App extends Component {
  constructor(){
    super();

    this.state = {
      amount: 0,
      lastDate: ''
    }
  }

  fetchData = () => {
    this.setState({
      amount:DATA.quotesAttempted, 
      lastDate:DATA.lastDate
    });
  }

  render() {
    return (
      <div className="App">
        <h5 id={"dataDisplay"}>Quotes attempted {this.state.amount} as of {this.state.lastDate}</h5>
        <Button 
          {...ButtonConfig} 
          handleClick={this.fetchData}
        />
      </div>
    );
  }
}

export default App;
