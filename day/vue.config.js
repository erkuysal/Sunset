const { defineConfig } = require('@vue/cli-service')
module.exports = {
    publicPath: 'http://localhost:8080', // The base URL your application bundle will be deployed at
    outputDir: '../night/static/dist', // The path for where files will be outputted when the app is built
    indexPath: '../../templates/_base_vue.html', // The path for the generated index.html file ?> in django app?

  configureWebpack: {
      devServer: {
        devMiddleware: {
          writeToDisk: true
        }
      }
  }
};
