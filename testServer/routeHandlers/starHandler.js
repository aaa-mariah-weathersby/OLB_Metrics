function starHandler(req,res,app) {
  let out = '<html><body><table><thead><tr><td>Method</td><td>URL</td></tr></thead>';
  app._router.stack.forEach(function (r) {
    if (r.route && r.route.path) {
      r.route.stack.forEach(function (rot) {
        let met = rot.method.toUpperCase();
        out = `${out}<tr><td>${met}</td><td>${r.route.path}</td>`;
      });
    }
  });

  const locals = (app.locals.ep3) ? JSON.stringify(app.locals.ep3) : '';

  out = `${out}</table><br>${locals}</body></html>`;
  res.setHeader('content-type', 'text/html');
  return res.send(out);
}

export default starHandler;