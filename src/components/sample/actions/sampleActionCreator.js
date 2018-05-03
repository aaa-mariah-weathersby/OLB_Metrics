
import {
  ActionTypes,
} from '../../../constants';

export default class SampleActionCreator {

  constructor() {
    this.sampleAction = this.sampleAction.bind(this);
    this.sampleExec = this.sampleExec.bind(this);
    this.sampleActionDelayed = this.sampleActionDelayed.bind(this);
  }

  sampleAction() {
    return {
      type: ActionTypes.SAMPLE_ACTION,
      payload: 'World!',
    };
  }

  sampleActionLoading() {
    return {
      type: ActionTypes.SAMPLE_LOADING,
    };
  }

  sampleActionDelayed() {
    const self = this;
    return (dispatch) => {
      dispatch(self.sampleActionLoading());
      setTimeout(() => {
        return dispatch(self.sampleAction());
      }, 2000);
    };
  }


  sampleNotification() {
    return {
      type: ActionTypes.SAMPLE_NOTIFY,
    };
  }

  sampleAsyncAction(data) {
    return {
      type: ActionTypes.SAMPLE_ASYNC,
      data,
    };
  }

  // does async delayed operation, returns a promise
  sampleExec() {
    const self = this;
    return (dispatch) => {
      dispatch(self.sampleNotification());
      // some long operation
      const promise = new Promise((resolve) => {
        setTimeout(() => {
          resolve({ sample: 'data' });
        }, 6000);
      });
      return promise.then((data) => {
        return dispatch(self.sampleAsyncAction(data));
      });
    };
  }

  // does an async delayed operation. does not return a promise
  sampleExec2() {
    const self = this;
    return (dispatch) => {
      dispatch(self.sampleNotification());
      setTimeout(() => {
        return dispatch(self.sampleAsyncAction({ sample: 'data' }));
      }, 199);
    };
  }

  // has background immediate operation, returns a promise
  sampleExec3() {
    const self = this;
    return (dispatch) => {
      dispatch(self.sampleNotification());
      // some long operation
      const promise = new Promise((resolve) => {
        resolve({ sample: 'data' });
      });
      return promise.then((data) => {
        return dispatch(self.sampleAsyncAction(data));
      });
    };
  }


}
