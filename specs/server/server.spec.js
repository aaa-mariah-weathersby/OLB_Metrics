import Chai from 'chai';
import ChaiHttp from 'chai-http';
import 'sinon-as-promised';
import Server from '../../server/server';

Chai.use(ChaiHttp);
Chai.should();

describe('Server', () => {
  it('Should send index.html', (done) => {
    Chai.request(Server)
      .get('/*')
      .end((err, res) => {
        res.should.have.status(200);
        done();
      });
  });
});
