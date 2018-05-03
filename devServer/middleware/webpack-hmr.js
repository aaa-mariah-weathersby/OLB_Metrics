import WebpackHotMiddleware from 'webpack-hot-middleware'

const debug = require('debug')('app:devServer:webpack-hmr')

export default function ({ compiler }) {
  debug('Enable Webpack Hot Module Replacement (HMR).')
  return WebpackHotMiddleware(compiler)
}

