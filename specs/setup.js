process.env.NODE_ENV = 'test';
process.env.APIC_BASE_URL = 'someAPICBaseURL';
process.env.WEB_SERVICE_API_BASE_URL = 'someWebServiceURL';
process.env.ACE_APIC_X_IBM_CLIENT_SECRET = 'someClientSecret';
process.env.ACE_APIC_X_IBM_CLIENT_ID = 'someClientID';
process.env.ACE_APIM_X_IBM_CLIENT_ID = 'someAPIMClientID';
process.env.ACE_APIM_X_IBM_CLIENT_SECRET = 'someAPIMClientSecret';
process.env.APIM_BASE_URL = 'someAPIMURL';
process.env.AUTH0_CERT_URL = 'someAuth0CertURL';
process.env.PORT = 1234;

import jsdom from 'jsdom';
import fetch from 'isomorphic-fetch';

const exposedProperties = ['window', 'navigator', 'document'];
global.fetch = fetch;

global.document = jsdom.jsdom('<body></body>', {
  url: 'https://uat2mvc.texas.aaa.com/aceapps/membership',
});
global.document.cookie = 'zipcode=80000|2222|252;';
global.window = document.defaultView;

Object.keys(document.defaultView).forEach((property) => {
  if (typeof global[property] === 'undefined') {
    exposedProperties.push(property);
    global[property] = document.defaultView[property];
  }
});

global.setupDocument = (url) => {
  const myurl = url || 'https://uat2mvc.texas.aaa.com/aceapps/membership';
  global.document = jsdom.jsdom('<body></body>', {
    url: myurl,
  });
  global.document.cookie = 'zipcode=80000|2222|252;';
  global.window = document.defaultView;

  Object.keys(document.defaultView).forEach((property) => {
    if (typeof global[property] === 'undefined') {
      exposedProperties.push(property);
      global[property] = document.defaultView[property];
    }
  });
};

global.event = {
  type: 'submit',
  preventDefault: () => { },
};

global.utag = { view: () => null };

global.aceMediaTagValues = {};

global.Payeezy = { callback: null };

global.navigator = {
  userAgent: 'node.js',
};


function noop() {
  return null;
}

function sessionStorageMock() {
  const storage = {};

  return {
    setItem(key, value) {
      storage[key] = value || '';
    },
    getItem(key) {
      return key in storage ? storage[key] : null;
    },
    removeItem(key) {
      delete storage[key];
    },
    get length() {
      return Object.keys(storage).length;
    },
    key(i) {
      const keys = Object.keys(storage);
      return keys[i] || null;
    },
  };
}

global.sessionStorage = sessionStorageMock();

require.extensions['.css'] = noop;
require.extensions['.scss'] = noop;
require.extensions['.less'] = noop;
require.extensions['.md'] = noop;
require.extensions['.png'] = noop;
require.extensions['.svg'] = noop;
require.extensions['.jpg'] = noop;
require.extensions['.jpeg'] = noop;
require.extensions['.gif'] = noop;
