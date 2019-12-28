/**
* This React class is intended to query an endpoint that will return an alphanumeric string, after clicking a button.
* This component is passed a prop "apiQueryDelay", which delays the endpoint request by N milliseconds. There is a 
* second button to disable this functionality and have the endpoint request run immediately after button click.
* This data is then to be displayed inside a simple container.
* The "queryAPI" XHR handler will return the endpoint response in the form of a Promise (such as axios, fetch).
* The response object will look like the following: {data: "A0B3HCJ"}
* The containing element ref isn't used, but should remain within the class.
* Please identify, correct and comment on any errors or bad practices you see in the React component class below.
* Additionally, please feel free to change the code style as you see fit.
* Please note - React version for this exercise is 15.5.4
*/

import React, { Component } from 'react';
import {queryAPI} from './queryAPI';
import {Button} from 'antd'


export class ShowResultsFromAPI extends Component {
  constructor(props) {
    super(props);
    this.state = {error: false, data: ''};
    this.container = null;
    this.fetchData = this.fetchData.bind(this);
  }

  onDisableDelay() {
    this.props.apiQueryDelay.delay = 0;
  }

  click() {
    let that = this;
      setTimeout(function () {
        that.fetchData();
      }, that.props.apiQueryDelay.delay);
  }

  fetchData() {
    let that = this;
    console.log("fetchData")
    queryAPI()
      .then(function (response) {
        console.log('data is ', response.data);
        if (response.data) {
          that.setState({
            data: response.data.data,
            error: false
          });
        }
      }).catch(function(err){
        console.log("Error", err)
      });
  }

  render() {
    return (
        <div>
        <div className="content-container" ref="container">
          {
            this.state.error ? (
              <p>Sorry - there was an error with your request.</p>
            ) : (
                <p>{this.state.data}</p>
            )
          }
        </div>
        <Button onClick={this.onDisableDelay.bind(this)}>Disable request delay</Button>
        <Button onClick={this.click.bind(this)}>Request data from endpoint</Button>
      </div>


    )
  }
}


ShowResultsFromAPI.displayName = {
  name: "ShowResultsFromAPI"
};


ShowResultsFromAPI.defaultProps = {
  apiQueryDelay: {delay: 2000}
};

// ShowResultsFromAPI.propTypes = {
//   apiQueryDelay: React.propTypes.number
// };

