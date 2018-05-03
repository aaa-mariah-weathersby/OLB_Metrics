import React from 'react';
import { mount, shallow, configure } from 'enzyme';
import Chai, { expect } from 'chai';
import sinon from 'sinon';
import Button from './button';
import Adapter from 'enzyme-adapter-react-16';

Chai.should();
configure({ adapter: new Adapter() });


describe('Button', () => {
  let handleClickSpy;
  let subject;
  let config;

  beforeEach(() => {
    handleClickSpy = sinon.spy();

    config = {
      title: "Get Quote Info",
      handleClick: handleClickSpy
    }

    subject = mount(<Button {...config}/>);
    
  });

  it('should render Button stateless component', () => {
    const buttonComponent = subject.find(Button);
    buttonComponent.length.should.eql(1);
  });

  it('should contain a button element', () => {
    const buttonElement = subject.find('button[type="button"]');
    buttonElement.length.should.eql(1);
  });

  it('should have a title', () => {
    const buttonTitle = subject.find(Button).text();
    const expectedTitle = config.title
    buttonTitle.should.eql(expectedTitle)
  });

  it.only('onClick should be called when button is clicked', () => {
    subject.find(Button).simulate('click');
    expect(handleClickSpy.calledOnce).to.be.true
  });


});