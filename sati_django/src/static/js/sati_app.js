(function () {
    'use strict';

    var app = angular.module('sati', [ 'crud-factory', 'sati-factory',
                                        // public
                                        'event-controller',
                                        // essencials
                                        'ngSanitize'
                                        ]);

    app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
    });


})(window.angular);