module.exports = function(config) {
  config.set({

    // base path that will be used to resolve all patterns (eg. files, exclude)
    basePath: '',

    preprocessors: {
      '../templates/*/*.html': ['ng-html2js'],
        'app/*.js': ['coverage']
    },
      // list of files / patterns to load in the browser
      files: [
            '../vendor/jquery/dist/jquery.js',
            '../vendor/angular/angular.min.js',
            '../vendor/angular/angular-route.min.js',
            '../vendor/angular/angular-mocks.js',
            '../vendor/angular/ui-bootstrap-tpls-0.13.0.min.js',
            '../vendor/angular-ui-select/dist/select.js',
            '../vendor/moment/min/moment-with-locales.min.js',
            '../templates/*/*.html',
            'app/app.js',
            'tests/*.js'
      ],


    // frameworks to use
    // available frameworks: https://npmjs.org/browse/keyword/karma-adapter
    frameworks: ['jasmine-jquery', 'jasmine'],


    // list of files to exclude
    exclude: [
    ],

    ngHtml2JsPreprocessor: {
      cacheIdFromPath: function (filepath) {
        var path = filepath.split('static');
        return '/static' + path[1];
      },
      //cacheIdFromPath: function(filepath) {
      //  alert(filepath);
      //  return filepath;
      //},
      // - setting this option will create only a single module that contains templates
      //   from all the files, so you can load them all with module('foo')
      // - you may provide a function(htmlPath, originalPath) instead of a string
      //   if you'd like to generate modules dynamically
      //   htmlPath is a originalPath stripped and/or prepended
      //   with all provided suffixes and prefixes
      moduleName: 'templates'
    },


    // test results reporter to use
    // possible values: 'dots', 'progress'
    // available reporters: https://npmjs.org/browse/keyword/karma-reporter
    reporters: ['progress', 'coverage'],


    // web server port
    port: 9876,


    // enable / disable colors in the output (reporters and logs)
    colors: true,


    // level of logging
    // possible values: config.LOG_DISABLE || config.LOG_ERROR || config.LOG_WARN || config.LOG_INFO || config.LOG_DEBUG
    logLevel: config.LOG_INFO,


    // enable / disable watching file and executing tests whenever any file changes
    autoWatch: true,


    // start these browsers
    // available browser launchers: https://npmjs.org/browse/keyword/karma-launcher
    browsers: ['PhantomJS'],


    // Continuous Integration mode
    // if true, Karma captures browsers, runs the tests and exits
    singleRun: false
  });
};
