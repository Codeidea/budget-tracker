var app = angular.module('app', []);

app.controller('TestController', function ($scope, $templateCache) {
    $scope.test = function () {
        $scope.abc = 'something';
    };
});

app.directive('aGreatEye', function () {
    return {
        restrict: 'E',
        replace: false,
        templateUrl: '/static/templates/expense/directive.html'
    };
});