import React from 'react';
import { shallow } from 'enzyme';
import { Route } from 'react-router';

import Routes from '../../src/routes';
import App from '../../src/components/app/app';
import SamplePage from '../../src/components/sample/containers/samplePage';
import ErrorPage from '../../src/components/app/errorPage';

describe('Routes', () => {
  let wrapper;
  let count;

  beforeEach(() => {
    wrapper = shallow(<Routes />);
    count = wrapper.find(Route).nodes.length;
  });

  it('create route for path "/app/" for App component', () => {
    wrapper.find(Route).nodes[1].props.path.should.eql('/');
    wrapper.find(Route).nodes[1].props.component.should.eql(App);
  });

  it('create route for path "sample" for Sample component', () => {
    wrapper.find(Route).nodes[2].props.path.should.eql('sample');
    wrapper.find(Route).nodes[2].props.component.should.eql(SamplePage);
  });

  // put all the route tests here

  // *-route test
  it('should route to error for invalid path', () => {
    wrapper.find(Route).nodes[count - 1].props.path.should.eql('*');
    wrapper.find(Route).nodes[count - 1].props.component.should.eql(ErrorPage);
  });
});
