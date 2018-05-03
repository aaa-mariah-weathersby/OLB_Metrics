import Chai from 'chai';
import Sinon from 'sinon';
import makeRootReducer from '../../src/store/reducers';
import * as Redux from 'redux';
import { routerReducer as router } from 'react-router-redux';
import samplePage from '../../src/components/sample/reducers/sampleReducer';

Chai.should();

describe('makeRootReducer', () => {
  let stubCombineReducers;
  beforeEach(() => {
    stubCombineReducers = Sinon.stub(Redux, 'combineReducers');
  });
  afterEach(() => {
    stubCombineReducers.restore();
  });

  it('should return correct reducers', () => {
    makeRootReducer();
    stubCombineReducers.withArgs({
      router,
      samplePage,
    }).calledOnce.should.be.true;
  });
});
