import React from 'react';
import { Route } from 'react-router';
import App from '../components/app/app';
import SamplePage from '../components/sample/containers/samplePage';
import ErrorPage from '../components/app/errorPage';
import { config } from '../config';

const path = config.baseDirectory;

export const createRoutes = (store) => (  // eslint-disable-line no-unused-vars
  <Route>
    <Route path={path} component={App}>
      <Route path="sample" component={SamplePage} />
      <Route path="*" component={ErrorPage} />
    </Route>
  </Route>
);

export default createRoutes;
