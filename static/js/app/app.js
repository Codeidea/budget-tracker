var App = angular.module('budget_tracker', [
    'ui.bootstrap',
    'ui.select',
    'ngRoute'
]);

App.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

App.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/create-expense', {
        templateUrl: '/static/templates/expense/create.html',
        controller: 'NewExpenseController'
    });

    $routeProvider.when('/expenses', {
        templateUrl: '/static/templates/expense/list.html',
        controller: 'ExpensesListController'
    });

}]);

App.controller('ExpensesListController', function ($scope, $http) {
    $scope.total_expenses = 0;
    $scope.expenses = [];

    $scope.filter = function (date) {
        var startDate = moment(date);
        var endDate = startDate.clone().add(1, 'month');

        $http.get(
            '/logs',
            { params: { date__gt: date, date__lt: endDate.format('YYYY-MM-DD') } }
        )
        .success(function (response) {
            $scope.expenses = response;

            var total = 0;
            $.each($scope.expenses, function (id, expense) {
                 total += parseFloat(expense.amount) * 100;
            });
            $scope.total_expenses = total / 100;
        });
    };

    $scope.filter(moment().date(1).format('YYYY-MM-DD'));
});

App.controller('NewExpenseController', function ($scope, $http, $sce, $location) {

    $scope.categories = [];
    $http.get('/log_categories').success(function (response) {
        $scope.categories = response;
    });

    $scope.trustAsHtml = $sce.trustAsHtml;

    $scope.create = function () {
        console.log($scope.data);
        $scope.data.amount = $scope.data.amount_zl + "." + $scope.data.amount_gr;
        $scope.data.date = moment($scope.data.date).format('YYYY-MM-DD');
        $scope.data.category = $scope.data.category_id.id;

        $http.post('/tracking', $scope.data).success(function (response) {
            $location.path('/expenses');
        });
    };

    $scope.cancel = function () {

    };

});

App.directive('logsDateFilter', function () {

    return {
        restrict: 'E',
        link: function ($scope, $element, attrs) {
            var now = moment().date(1);
            var lastMonth = now.clone().subtract(1, 'month');
            var monthBeforeLastMonth = lastMonth.clone().subtract(1, 'month');

            $scope.buttons = [
                { date: monthBeforeLastMonth.format('YYYY-MM-DD'), text: monthBeforeLastMonth.format('MMMM') },
                { date: lastMonth.format('YYYY-MM-DD'), text: lastMonth.format('MMMM') },
                { date: now.format('YYYY-MM-DD'), text: 'This month' }
            ];
        },
        templateUrl: '/static/templates/logs/date-filter.html'
    };

});

App.filter('momentjs', function () {
    return function (dateString, formatting) {
        if (!formatting) {
            throw new Error('Missing format argument for filter momentjs');
        }

        return moment(dateString).format(formatting);
    };
});

