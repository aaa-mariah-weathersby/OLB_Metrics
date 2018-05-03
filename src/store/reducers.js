import { combineReducers } from 'redux';
import { routerReducer as router } from 'react-router-redux';
import samplePage from '../components/sample/reducers/sampleReducer';

export const makeRootReducer = (asyncReducers) => {
  const combinedReducers = { ...asyncReducers, router, samplePage };

  return combineReducers(
    combinedReducers
  );
};

export default makeRootReducer;
