import Chai from 'chai';
import { ActionTypes } from '../../../../src/constants';
import Sinon from 'sinon';

import reducer from '../../../../src/components/sample/reducers/sampleReducer';
import middleware from '../../../../src/components/sample/middleware/sampleMiddleware';

Chai.should();

describe('sample middleware', () => {
  let stubDispatch;
  let stubGetState;
  let myStore;
  let myNext;
  let myState;

  beforeEach(() => {
    stubDispatch = Sinon.spy();
    stubGetState = Sinon.stub();
    myState = reducer(undefined, {});
    stubGetState.returns({
      ...myState,
    });
    myStore = { dispatch: stubDispatch, getState: stubGetState };
    myNext = Sinon.spy();
  });

  it('SAMPLE_ACTION', () => {
    middleware(myStore)(myNext)({
      type: ActionTypes.SAMPLE_ACTION,
      payload: 'World!',
    });
    myNext.withArgs({
      type: ActionTypes.SAMPLE_ACTION,
      payload: 'World!',
      sampleMessage: 'Hello World!',
    }).calledOnce.should.be.true;
  });
});
