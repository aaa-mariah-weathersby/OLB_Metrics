import {
  ActionTypes,
} from '../../../constants';

export default function samplePageReducer(
  state = {
    sampleMessage: '',
    messageLoading: false,
  }, action
) {
  switch (action.type) {
    case ActionTypes.SAMPLE_ACTION:
      return { ...state, sampleMessage: action.sampleMessage, messageLoading: false };

    case ActionTypes.SAMPLE_NOTIFY:
      return { ...state, completed: false };

    case ActionTypes.SAMPLE_ASYNC:
      return { ...state, payload: action.data, completed: true };

    case ActionTypes.SAMPLE_LOADING:
      return { ...state, messageLoading: true };

    default:
      return state;
  }
}
