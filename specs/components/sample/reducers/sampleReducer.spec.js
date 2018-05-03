import Chai from 'chai';
import reducer from '../../../../src/components/sample/reducers/sampleReducer';
import {
  ActionTypes,
} from '../../../../src/constants';

Chai.should();

describe('Sample reducer', () => {
  let initialState;

  beforeEach(() => {
    initialState = {
      sampleMessage: '',
      messageLoading: false,
    };
  });

  it('Initial state', () => {
    reducer(undefined, {}).should.eql(initialState);
  });

  it('SAMPLE_ACTION', () => {
    reducer(initialState, {
      type: ActionTypes.SAMPLE_ACTION,
      sampleMessage: 'test',
    }).should.eql({
      sampleMessage: 'test',
      messageLoading: false,
    });
  });

  it('SAMPLE_NOTIFY', () => {
    reducer(initialState, {
      type: ActionTypes.SAMPLE_NOTIFY,
    }).should.eql({
      sampleMessage: '',
      messageLoading: false,
      completed: false,
    });
  });

  it('SAMPLE_ASYNC', () => {
    reducer(initialState, {
      type: ActionTypes.SAMPLE_ASYNC,
      data: 'data',
    }).should.eql({
      sampleMessage: '',
      messageLoading: false,
      completed: true,
      payload: 'data',
    });
  });
});
