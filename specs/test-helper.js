/* eslint-disable */
import React from 'react';

class TestHelper {

  createComponentWithStubbedContext(Component, props) {
    return React.createClass({
      childContextTypes : {
        insertCss:React.PropTypes.func,
        setTitle:React.PropTypes.func,
        setMeta:React.PropTypes.func,
      },
      getChildContext(){
        return {
          insertCss: () => {},
          setTitle: () => {},
          setMeta: () => {},
        };
      },
      render(){
        return(<Component {...props}/>);
      }
    });
  }

  createFakeComponentWithContextTypes() {
    return React.createClass({
      contextTypes: {
        insertCss: React.PropTypes.func,
        setTitle: React.PropTypes.func,
        setMeta: React.PropTypes.func,
      },
      render() {
        return (<div></div>);
      },
    });
  }
}

export default new TestHelper();
