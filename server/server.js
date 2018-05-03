import express from 'express';
import path from 'path';
import cookieParser from 'cookie-parser';
import helmet from 'helmet';
import { port } from '../src/config';
import fetch from 'isomorphic-fetch';
import bodyParser from 'body-parser';
import csrf from 'csurf';

// console.log('>>>SERVER port:', port);

var app = express();
app.use(cookieParser());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
  extended: true,
}));

if (process.env.NODE_ENV !== 'test') {
  app.use(csrf({ cookie: { secure: true, httpOnly: true } }));
}

app.use(function (err, req, res, next) {
  if (err.code !== 'EBADCSRFTOKEN') {
    aceLogger('Error in CSRF token: ', err);
    return next(err);
  }

  // handle CSRF token errors here 
  const results = {
    message: 'form was tampered with',
  };
  res.status(403);
  res.send(results);
});

app.use(helmet());

app.use(express.static(path.join(__dirname, 'public'), { maxAge: 31557600000 }));

app.use('/*', function (req, res, next) {
  res.setHeader('Cache-Control', 'private, no-cache, no-store, must-revalidate');
  res.setHeader('Expires', '-1');
  res.setHeader('Pragma', 'no-cache');
  res.setHeader('X-Frame-Options', 'SAMEORIGIN');
  res.setHeader('X-XSS-Protection', '1');
  next();
});

app.get('/*', (req, res) => {
  if (req.csrfToken) {
    res.cookie('csrft', req.csrfToken({ secure: true }));
  }
  return res.sendFile(path.join(__dirname, 'public/index.html'));
});

const server = app.listen(port, () => {
  const host = server.address().address;
  const port = server.address().port;
});

export default app;
