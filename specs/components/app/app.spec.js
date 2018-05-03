import React from 'react';
import { mount } from 'enzyme';
import Chai from 'chai';
import TestHelper from '../../test-helper';
import { App } from '../../../src/components/app/app';
import configureStore from 'redux-mock-store';
import emptyFunction from 'fbjs/lib/emptyFunction';

Chai.should();

describe('<App/>', () => {
  let FakeComponent;

  beforeEach(() => {
    FakeComponent = TestHelper.createFakeComponentWithContextTypes();
  });

  describe('component map state to props', () => {
  });

  describe('render()', () => {
    let subject;
    let configureMockStore;
    let mockStore;
    let componentContext;
    let routes;

    beforeEach(() => {
      configureMockStore = configureStore();
      mockStore = configureMockStore({});

      componentContext = {
        store: mockStore,
        insertCss: emptyFunction,
        setTitle: emptyFunction,
        setMeta: emptyFunction,
      };

      routes = require('../../../src/routes/index').default(mockStore);

      subject = mount(<App
        context={componentContext}
        children={routes}
      ><FakeComponent /></App>);
      document.cookie = 'aceclb=004';
    });

    it('should render App component', () => {
      const instance = subject.instance();
      instance.should.be.an.instanceOf(App);
    });

    it('should render correct child component', () => {
      subject.props().children.should.eql(<FakeComponent />);
    });
  });
});
