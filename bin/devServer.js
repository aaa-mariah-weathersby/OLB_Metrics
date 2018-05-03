import config from '../config';
import server from '../devServer/main';
import _debug from 'debug';

const debug = _debug('app:bin:devServer');
const port = config.server_port;

server.listen(port, () => {
  debug(`Server is now running at : ${port}.`);
});
