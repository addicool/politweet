import React, { Component } from 'react';
import StatItem from './stat_item';


class StatContainer extends Component {
  constructor() {
    super();
  }

  render() {
    return (
      <div className="theStatListContainer">
        <ul className="theStatListContainer">
          <StatItem selectedFighter={this.props.selectedFighter}/>
        </ul>
      </div>
    );
  }
}

export default StatContainer;
