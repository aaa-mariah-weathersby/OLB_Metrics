import { applyMiddleware, createStore } from 'redux';
import thunk from 'redux-thunk';
import makeRootReducer from './reducers';
// import createLogger from 'redux-logger';

import sampleMiddleware from '../components/sample/middleware/sampleMiddleware';

export default (initialState = {}, history) => { // eslint-disable-line no-unused-vars
  // ======================================================
  // Middleware Configuration
  // ======================================================
  const middleware = [
    thunk,
    sampleMiddleware,
  ];

  if (process.env.NODE_ENV !== 'production') {
    const createLogger = require('redux-logger');
    middleware.push(createLogger());
  }

  // ======================================================
  // Store Instantiation and HMR Setup
  // ======================================================
  const store = createStore(
    makeRootReducer(),
    initialState,
    applyMiddleware(...middleware)
  );

  return store;
};
