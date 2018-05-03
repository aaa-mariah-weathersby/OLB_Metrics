import Chai from 'chai';
import CookieHelper from '../../src/utils/cookieHelper';

Chai.should();

describe('cookieHelper', () => {
  describe('getCookie', () => {
    context('When cookie is coming from request', () => {
      let fakeRequest;
      let expectedValue;

      beforeEach(() => {
        fakeRequest = {
          cookies: {
            someCookie: 'someValue',
          },
        };
      });

      it('should get a cookie value', () => {
        expectedValue = CookieHelper.getCookie('someCookie', fakeRequest);
        expectedValue.should.equal('someValue');
      });
    });

    context('When ACE cookie exists', () => {
      beforeEach(() => {
        document.cookie = 'somecookie=; expires=Thu, 01 Jan 1970 00:00:00 UTC;';
        document.cookie = 'aceclb=; expires=Thu, 01 Jan 1970 00:00:00 UTC;';
        document.cookie = 'aceclb=club';
      });
      it('should get a cookie value', () => {
        const club = CookieHelper.getCookie('aceclb');
        club.should.equal('club');
      });
    });

    context('When ACE cookie doesn\'t exists', () => {
      beforeEach(() => {
        document.cookie = 'somecookie=; expires=Thu, 01 Jan 1970 00:00:00 UTC;';
        document.cookie = 'aceclb=; expires=Thu, 01 Jan 1970 00:00:00 UTC;';
        document.cookie = 'somecookie=value';
      });
      it('should not get a cookie value', () => {
        const club = CookieHelper.getCookie('aceclb');
        Chai.expect(club).to.be.null;
      });
    });
  });
});
