import ecosystem from '../build/ecosystem';
import fs from 'fs';

function doit(env) {
  const result = {
    apps: [{
      env: {},
    }],
    deploy: {},
  };

  ecosystem.apps.forEach((appsitem) => {
    Object.keys(appsitem).forEach((key) => {
      const itemval = appsitem[key];
      Object.keys(itemval).forEach((key2) => {
        const envval = itemval[key2];
        if (key2 === 'NODE_ENV' && envval === env) {
          result.apps[0].name = appsitem.name;
          result.apps[0].script = appsitem.script;
          result.apps[0].env = appsitem.env;
          Object.assign(result.apps[0].env, itemval);
        }
      });
    });
  });

  Object.keys(ecosystem.deploy).forEach((item) => {
    const deployitem = ecosystem.deploy[item];
    if (deployitem.env.NODE_ENV === env) {
      result.deploy[item] = deployitem;
    }
  });

  const ecosystemfile = __dirname + '/../build/ecosystem.' + env + '.json';
  fs.writeFileSync(ecosystemfile, JSON.stringify(result, null, 2));
  const ecosystemOriginfile = __dirname + '/../build/ecosystem.json';
  fs.unlinkSync(ecosystemOriginfile);
  const ecosystemtmp = __dirname + '/../build/ecosystem.js';
  fs.unlinkSync(ecosystemtmp);
};

export default doit;
