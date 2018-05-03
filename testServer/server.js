import express from 'express';
import path from 'path';
import cookieParser from 'cookie-parser';
import { port } from '../src/config';
import { EndPoints, RouteNames } from '../src/constants';
import bodyParser from 'body-parser';
// internal API
import setHandler from './routeHandlers/setHandler';
import starHandler from './routeHandlers/starHandler';

var app = express();
app.use(cookieParser());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
  extended: true,
}));

app.use((req, res, next) => {
  console.log('\nTestServer path:', req.path);
  if (!app.locals.ep3) app.locals.ep3 = {};
  next();
});

app.get('/set', (req, res) => {
  setHandler(req, res, app);
});

app.get('/reset', (req, res) => {
  app.locals.ep3 = {};
  starHandler(req, res, app);
});

app.get('/help', (req, res) => {
  return res.sendFile(path.join(__dirname, 'public/help.html'));
});

app.use('/*', (req, res, next) => {
  res.setHeader('Cache-Control', 'private, no-cache, no-store, must-revalidate');
  res.setHeader('Expires', '-1');
  res.setHeader('Pragma', 'no-cache');
  res.setHeader('X-Frame-Options', 'SAMEORIGIN');
  res.setHeader('X-XSS-Protection', '1');
  next();
});

app.get('/*', (req, res) => {
  starHandler(req, res, app);
});

const server = app.listen(port, () => {
  console.log('Listenting on port', server.address().port, 'host:', server.address().address);
});

export default app;
