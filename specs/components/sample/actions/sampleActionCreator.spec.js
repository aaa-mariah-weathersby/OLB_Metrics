import Chai from 'chai';
import configureMockStore from 'redux-mock-store';
import thunk from 'redux-thunk';
import Sinon from 'sinon';

import SampleActionCreator from '../../../../src/components/sample/actions/sampleActionCreator';
import reducer from '../../../../src/components/sample/reducers/sampleReducer';
import middleware from '../../../../src/components/sample/middleware/sampleMiddleware';

import { ActionTypes } from '../../../../src/constants';

Chai.should();

describe('SampleActionCreator', () => {
  let subject;
  beforeEach(() => {
    subject = new SampleActionCreator();
  });

  afterEach(() => {

  });

  it('Should return a proper action', () => {
    const result = subject.sampleAction();
    result.should.eql({
      type: ActionTypes.SAMPLE_ACTION,
      payload: 'World!',
    });
  });

  context('Dispatch action', () => {
    let defaultState;
    let mockStore;
    let store;
    let actions;

    beforeEach(() => {
      defaultState = reducer(undefined, {});
      mockStore = configureMockStore([thunk, middleware]);
      store = mockStore(defaultState);
    });

    it('SAMPLE_ACTION', () => {
      store.dispatch(subject.sampleAction());
      actions = store.getActions();
      actions.should.eql([
        {
          type: ActionTypes.SAMPLE_ACTION,
          payload: 'World!',
          sampleMessage: 'Hello World!',
        },
      ]);
    });

    // notice "done" which is a callbeck we need to call at the end of the test
    it('sampleExec3 using setTimeout', (done) => {
      store.dispatch(subject.sampleExec3());
      actions = store.getActions();
      // READ THIS CAREFULLY
      // at this point there will be only 1 action instead of the two
      // which is not what we're expecting in this test
      actions.should.eql([
        {
          type: ActionTypes.SAMPLE_NOTIFY,
        },
      ]);

      // we cannot test like this, we need to use setTimeout below
      // if an action is returning a promise we can use .then() instead of the setTimeout

      // setTimeout is necessary to allow a background thread to finish
      setTimeout(() => {
        actions = store.getActions();
        actions.should.eql([
          {
            type: ActionTypes.SAMPLE_NOTIFY,
          },
          {
            type: ActionTypes.SAMPLE_ASYNC,
            data: {
              sample: 'data',
            },
          },
        ]);
        done();
      }, 1);
    });
    it('sampleExec3 using then', (done) => {
      // action returns a promise, we don't need to use setTimeout
      store.dispatch(subject.sampleExec3()).then(() => {
        actions = store.getActions();
        actions.should.eql([
          {
            type: ActionTypes.SAMPLE_NOTIFY,
          },
          {
            type: ActionTypes.SAMPLE_ASYNC,
            data: {
              sample: 'data',
            },
          },
        ]);
        done();
      });
    });

    context('sampleExec using then and faketimers', () => {
      let timers;
      beforeEach(() => {
        timers = Sinon.useFakeTimers();
      });
      afterEach(() => {
        timers.restore();
      });
      it('sampleExec using then', (done) => {
        // action returns a promise, we don't need to use setTimeout

        const promise = store.dispatch(subject.sampleExec());
        timers.tick(6000);

        promise.then(() => {
          actions = store.getActions();
          actions.should.eql([
            {
              type: ActionTypes.SAMPLE_NOTIFY,
            },
            {
              type: ActionTypes.SAMPLE_ASYNC,
              data: {
                sample: 'data',
              },
            },
          ]);
          done();
        });
      });
    });

    context('sampleExec2 with timers', () => {
      let timers;
      beforeEach(() => {
        timers = Sinon.useFakeTimers();
      });
      afterEach(() => {
        timers.restore();
      });

      it('Exec using then2', (done) => {
        // action does not return a promise, we cannot use .then
        store.dispatch(subject.sampleExec2());
        timers.tick(199);
        actions = store.getActions();
        actions.should.eql([
          {
            type: ActionTypes.SAMPLE_NOTIFY,
          },
          {
            type: ActionTypes.SAMPLE_ASYNC,
            data: {
              sample: 'data',
            },
          },
        ]);

        done();
      });
    });
  });
});
