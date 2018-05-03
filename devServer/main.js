import express from 'express';
// import exressSession from 'express-session';
import path from 'path';
import cookieParser from 'cookie-parser';
import historyApiFallback from 'connect-history-api-fallback';
import webpackConfig from '../tools/webpack.config';
import webpack from 'webpack';
import config from '../config';
import webpackDevMiddleware from './middleware/webpack-dev';
import webpackHMRMiddleware from './middleware/webpack-hmr';

// import HttpDispatcher from '../src/utils/httpDispatcher';
import fetch from 'isomorphic-fetch';
import bodyParser from 'body-parser';
import csrf from 'csurf';

const paths = config.utils_paths;
const app = express();
app.use(cookieParser());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
  extended: true,
}));

app.use(function (err, req, res, next) {
  if (err.code !== 'EBADCSRFTOKEN') {
    console.log('Error in CSRF token: ', err);
    return next(err);
  }

  // handle CSRF token errors here 
  const results = {
    message: 'form was tampered with',
  };
  res.status(403);
  res.send(results);
});

app.use((req, res, next) => {
  if (!app.locals.ep3) app.locals.ep3 = {};
  for (let key in req.query) {
    app.locals.ep3[key] = req.query[key];
  }
  next();
});

app.use('/*', (req, res, next) => {
  console.log(`\n`);
  // console.log('>>> DEVSERVER MOCK: client\'s IP:', req.connection.remoteAddress);
  // console.log('>>> DEVSERVER MOCK: headers', req.headers);
  // console.log('>>> DEVSERVER MOCK: request', req);
  // console.log('>>> query', req.query);

  res.setHeader('Cache-Control', 'private, no-cache, no-store, must-revalidate');
  res.setHeader('Expires', '-1');
  res.setHeader('Pragma', 'no-cache');
  // res.setHeader('X-Frame-Options', 'SAMEORIGIN');
  next();
  // res.send(`client\'s IP:' + ${req.connection.remoteAddress} + 'forwarded for: ' + ${req.headers['x-forwarded-for']}`);
});


// ************ CSRF protected stuff ***********************

app.use(csrf({ cookie: { secure: false, httpOnly: true } }));

app.get('/help', (req, res) => {
  return res.sendFile(path.join(__dirname, 'help.html'));
});

app.get('/endpoints', (req, res) => {
  let out = '<html><body><table><thead><tr><td>Method</td><td>URL</td></tr></thead>';
  app._router.stack.forEach(function (r) {
    if (r.route && r.route.path) {
      r.route.stack.forEach(function (rot) {
        let met = rot.method.toUpperCase();
        out = `${out}<tr><td>${met}</td><td>${r.route.path}</td>`;
      });
    }
  });
  out = `${out}</table></body></html>`;
  res.setHeader('content-type', 'text/html');
  return res.send(out);
});

app.get('/*', (req, res, next) => {
  console.log('>>>DEVSERVER path:', req.path);

  if (app.locals.ep3.aceclb) {
    res.cookie('aceclb', app.locals.ep3.aceclb);
  }
  if (app.locals.ep3.aceut) {
    console.log('set aceut cookie');
    res.cookie('aceut', app.locals.ep3.aceut);
  }
  if (!app.locals.ep3.zipcode) {
    app.locals.ep3.zipcode = '90000|2222|252';
  }
  res.cookie('zipcode', app.locals.ep3.zipcode, { encode: (str) => { return str; } });
  res.cookie('csrft', req.csrfToken());

  next();
});

// This rewrites all routes requests to the root /index.html file
// (ignoring file requests). If you want to implement isomorphic
// rendering, you'll want to remove this middleware.
app.use(historyApiFallback({
  verbose: false,
}));

// ------------------------------------
// Apply Webpack HMR Middleware
// ------------------------------------
if (config.env === 'development') {
  // Enable webpack-dev and webpack-hot middleware
  const { publicPath } = webpackConfig.output;
  const compiler = webpack(webpackConfig);

  app.use(webpackDevMiddleware({ compiler, publicPath }));
  app.use(webpackHMRMiddleware({ compiler }));

  app.use(express.static(paths.client('assets')));
} else {
  app.use(express.static(paths.dist()));
}

export default app;
