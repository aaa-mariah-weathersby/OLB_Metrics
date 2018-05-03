import React from 'react';
import ReactDOM from 'react-dom';
import { mount, shallow, configure } from 'enzyme';
import Chai, { expect } from 'chai';
import sinon from 'sinon';
import App from './App';
import Button from './components/common/button/button';
import Adapter from 'enzyme-adapter-react-16';

import DATA from './data-huon.json'

Chai.should();
configure({ adapter: new Adapter() });

describe('App', () => {
  let subject;

  beforeEach(() => {
    subject = mount(<App/>);
    
  });

  it('should render App', () => {    
    const component = subject.find(App);
    component.length.should.eql(1);
  });

  it('should render Button', () => {    
    const component = subject.find(Button);
    component.length.should.eql(1);
  });


  it('should call fetchData method exists', () => {
    const component = subject.instance();
    var componentStub = sinon.stub(component, "fetchData");
    component.fetchData()

    componentStub.calledOnce.should.eql(true)
  });

  it('should verify state after fetchData call', () => {
    const component =  subject.instance();
    const componentState = component.state;
    const expectedState = { 'amount':DATA.quotesAttempted, 'lastDate':DATA.lastDate }
    
    subject.instance().fetchData()
    
    JSON.stringify(expectedState).should.eql(JSON.stringify(subject.instance().state))

  });

  it('should contain text element', () => {
    const element = subject.find('#dataDisplay');
    element.length.should.eql(1);
  })

  it('text element should display data', () => {
    const component = subject.instance();
    subject.instance().fetchData();

    const element = subject.find('#dataDisplay');
    const elementText = element.text();

    const returnedQuotes = component.state.amount;
    const returnedDate = component.state.lastDate;

    const expectedText = 
      `Quotes attempted ${returnedQuotes} as of ${returnedDate}`;

    elementText.should.eql(expectedText);
  })

});
