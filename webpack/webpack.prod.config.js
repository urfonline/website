const webpack = require('webpack');
const config = require('./webpack.base.config.js');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

const SaveAssetsJson = require('assets-webpack-plugin');

config.bail = true;
config.profile = false;
config.devtool = '#source-map';

config.output = {
  path: './assets/dist',
  publicPath: '/assets/',
  filename: '[name].[hash].min.js',
};

config.plugins = config.plugins.concat([
  new webpack.optimize.UglifyJsPlugin(),
  new SaveAssetsJson({
    path: './assets/dist/',
    filename: 'assets.json',
  }),
]);


module.exports = config;