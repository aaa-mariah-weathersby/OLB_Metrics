/* eslint-disable react/prefer-stateless-function */
import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import s from '../../styles/core.scss';

export class App extends React.Component {

  static propTypes = {
    children: React.PropTypes.element.isRequired,
  };

  static contextTypes = {
    router: PropTypes.object,
  };

  render() {
    return (
      <div className={s.app}>
        <header>
        </header>
        <content className={s.content}>
          {this.props.children}
        </content>
        <footer>
        </footer>
      </div>
    );
  }
}

export function mapStateToProps(state) { // eslint-disable-line no-unused-vars
  return {};
}

const mapActionCreators = {};

export default connect(mapStateToProps, mapActionCreators)(App);
