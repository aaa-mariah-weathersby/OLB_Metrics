import WebpackDevMiddleware from 'webpack-dev-middleware'
import config from '../../config'

const paths = config.utils_paths
const debug = require('debug')('app:devServer:webpack-dev')

export default function ({ compiler, publicPath }) {
  debug('Enable Webpack dev middleware.')

  return WebpackDevMiddleware(compiler, {
    publicPath,
    contentBase: paths.client(),
    hot: true,
    quiet: config.compiler_quiet,
    noInfo: config.compiler_quiet,
    lazy: false,
    stats: config.compiler_stats
  })
}
