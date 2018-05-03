/* eslint-disable react/prefer-stateless-function */
/* eslint-disable max-len */
import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import SampleActionCreator from '../actions/sampleActionCreator';

const samplePageActionCreator = new SampleActionCreator();

export class SamplePage extends React.Component {
  static propTypes = {
    sampleMessage: PropTypes.string,
    sampleAction: PropTypes.func,
    sampleLoading: PropTypes.bool,
  }

  constructor(props) {
    super(props);
    this.onClick = this.onClick.bind(this);
  }

  onClick() {
    this.props.sampleAction();
  }

  render() {
    // console.log('>>> props:', this.props);

    const myMessage = (this.props.sampleLoading) ? 'Loading....' : this.props.sampleMessage;

    return (
      <div style={{ textAlign: 'center' }}>
        <h1>Sample page</h1>
        <span
          id="idSpan"
          style={{
            border: '1px darkgray solid', width: 'calc(100% - 32px)', padding: '17px', display: 'block', margin: '16px',
            textAlign: 'center', fontSize: '18px',
          }}
        >[{myMessage}]</span>
        <div className="buttonContainer">
          <div id="idButton" onClick={this.onClick} className={'button optionButton'}>Click Me</div>
        </div>
      </div>
    );
  }
}

export function mapStateToProps(state) {
  return {
    sampleMessage: state.samplePage.sampleMessage,
    sampleLoading: state.samplePage.messageLoading,
  };
}

const mapActionCreators = {
  sampleAction: samplePageActionCreator.sampleActionDelayed,
};

export default connect(mapStateToProps, mapActionCreators)(SamplePage);
