import HttpDispatcher from '../../src/utils/httpDispatcher';
import CookieHelper from '../../src/utils/cookieHelper';
import Chai from 'chai';
import Sinon from 'sinon';
import nock from 'nock';
import _ from 'lodash';
const cap = require('chai-as-promised');
Chai.should();
Chai.use(cap);

describe('HttpDispatcher', () => {
  let httpDispatcher;
  let promise;
  let error;

  beforeEach(() => {
    httpDispatcher = new HttpDispatcher();
    error = { error: 'someerror' };
  });

  describe('processRequest(url, options)', () => {
    let result;
    beforeEach(() => {
      result = { title: 'some title' };
      nock('https://somedomain.com')
      .get('/success200')
      .reply(200, result);

      nock('https://somedomain.com')
      .get('/successAsync')
      .reply(200, JSON.stringify(result));

      nock('https://somedomain.com')
        .get('/error400')
        .reply(400, JSON.stringify(error), { 'Content-Type': 'application/json' });

      nock('https://somedomain.com')
        .get('/error500')
        .reply(500, JSON.stringify(error), { 'Content-Type': 'application/json' });

      nock('https://somedomain.com')
        .get('/timeout')
        .socketDelay(10);
    });

    context('When promise resolves successfully (http status = 200)', () => {
      it('should get successful response', (done) => {
        const url = 'https://somedomain.com/success200';
        const options = {};

        promise = httpDispatcher.processRequest(url, options);
        promise.then((res) => {
          _.isEqual(res, result).should.be.true; // eslint-disable-line no-unused-expressions
          done();
        });
      });

      it('should get successful response using async call', (done) => {
        promise = httpDispatcher.processRequest('https://somedomain.com/successAsync', {}, true);
        promise.then((json) => {
          json.json().then(jsondata => {
            jsondata.should.eql.result;
            done();
          });
        });
      });
    });

    context('When promise rejected with error (http status = 400)', () => {
      it('should resolve with an error', () => {
        const url = 'https://somedomain.com/error400';
        const options = {};
        // promise = httpDispatcher.processRequest(url, options);
        // return promise.catch((error) => {
        //   error.message.should.equal('400');
        // });
        promise = httpDispatcher.processRequest(url, options);
        return promise.catch((err) => {
          JSON.stringify(err).should.equal(JSON.stringify(error));
        });
      });
    });

    context('When promise rejected with error (http status = 500)', () => {
      it('should resolve with an error', () => {
        const url = 'https://somedomain.com/error500';
        const options = {};
        // promise = httpDispatcher.processRequest(url, options);
        // return promise.catch((error) => {
        //   error.message.should.equal('500');
        // });
        promise = httpDispatcher.processRequest(url, options);
        return promise.catch((err) => {
          JSON.stringify(err).should.equal(JSON.stringify(error));
        });
      });
    });

    context('When request times out', () => {
      it('should handle a timeout', () => {
        const url = 'https://somedomain.com/timeout';
        const options = { timeout: 1 };
        promise = httpDispatcher.processRequest(url, options);
        return promise.should.eventually.be.rejectedWith(Error);
      });
    });
  });

  describe('processRequest with stubbed fetch method', () => {
    let stubFetch;
    let fakeURL;
    let stubOptions;
    let stubCookieHelper;
    let stubFetchResponse;
    let expectedOptions;

    beforeEach(() => {
      stubFetch = Sinon.stub(global, 'fetch');
      stubFetchResponse = {
        json: () => new Promise((resolve) => {
          resolve({ json: 'someJSON' });
        }),
        ok: true,
      };
      stubFetch.resolves(Promise.resolve(stubFetchResponse));
      fakeURL = 'http://moogle.com';
      stubOptions = {
        method: 'POST',
        headers: {
        },
      };
      expectedOptions = {
        method: 'POST',
        credentials: 'include',
        headers: {
          'x-csrf-token': 'someCSRFToken',
        },
      };
      stubCookieHelper = Sinon.stub(CookieHelper, 'getCookie');
      stubCookieHelper.returns('someCSRFToken');
    });
    afterEach(() => {
      stubFetch.restore();
      stubCookieHelper.restore();
    });

    it('should append x-csrf-token to options for a Method call', () => httpDispatcher.processRequest(fakeURL, stubOptions).then(() => {
      stubFetch.calledWith(fakeURL, expectedOptions).should.be.true;
    }));
  });
});
