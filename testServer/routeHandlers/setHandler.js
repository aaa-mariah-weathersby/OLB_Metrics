import starHandler from './starHandler';

function setHandler(req,res,app) {
  for (let key in req.query) {
    app.locals.ep3[key] = req.query[key];
  }
  starHandler(req,res,app);
}

export default setHandler;