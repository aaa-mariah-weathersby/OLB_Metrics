const webpackConfig = {
  entry: './testServer/server.js',
  output: {
    path: 'build',
    filename: 'server.js',
  },
  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel', // 'babel-loader' is also a legal name to reference
        query: {
          presets: ['env'],
          compact: true,
        },
      },
      {
        test: /\.json$/,
        loader: 'json-loader',
      },
    ],
  },
  node: {
    console: 'empty',
    fs: 'empty',
    net: 'empty',
    tls: 'empty',
    __dirname: false,
    __filename: false,
  },
  target: 'node',
};


module.exports = webpackConfig;
