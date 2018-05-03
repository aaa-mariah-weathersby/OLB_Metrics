import {
  ActionTypes,
} from '../../../constants';
/* eslint-disable no-param-reassign */
const SampleMiddleware = store => next => action => {
  const state = store.getState();
  switch (action.type) {
    case ActionTypes.SAMPLE_ACTION:
      if (!state.messageAssigned) {
        action.sampleMessage = `Hello ${action.payload}`;
      }
      break;

    default:
      break;
  }
  return next(action);
};

export default SampleMiddleware;
