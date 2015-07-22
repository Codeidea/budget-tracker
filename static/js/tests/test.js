describe('Filter tests', function () {

    beforeEach(module('budget_tracker'));

    var $filter;
    beforeEach(inject(function (_$filter_) {
        $filter = _$filter_;
    }));

    describe('momentjs filter should', function () {

        it ('apply given formatting to provided date string', function () {
            var momentjs = $filter('momentjs');
            expect(momentjs('2015-01-07', 'YYYY')).toBe('2015');
        });

        it('throw an error if formatting is not specified', function () {
            var momentjs = $filter('momentjs');
            expect(function () { momentjs('2015-01-07') }).toThrow(new Error('Missing format argument for filter momentjs'));
        });

    });

});

describe('ControllerTests', function () {

    beforeEach(module('budget_tracker'));

    var $controller;
    var $httpBackend;
    var categoriesRequestHandler;

    beforeEach(inject(function (_$controller_, _$httpBackend_) {
        $controller = _$controller_;
        $httpBackend = _$httpBackend_;

        categoriesRequestHandler = $httpBackend.when('GET', '/log_categories').respond([{id: 1, name: 'Category', key: 'category'}]);
    }));

    afterEach(function() {
        $httpBackend.verifyNoOutstandingExpectation();
        $httpBackend.verifyNoOutstandingRequest();
    });

    describe('testing main controller', function () {

        it ('should fetch categories to display in form', function () {
            var $scope = {};
            $httpBackend.expectGET('/log_categories');
            $controller('NewExpenseController', { $scope: $scope });
            $httpBackend.flush();

            expect($scope.categories[0]['name']).toBe('Category');
        });

    });

});

describe('Testing directive', function () {
    var $compile, $rootScope;

    beforeEach(function () {
        module('budget_tracker');
        module('templates');
    });

    beforeEach(inject(function(_$compile_, _$rootScope_) {
        $compile = _$compile_;
        $rootScope = _$rootScope_;
    }));


    it('should work', function () {
        jasmine.clock().mockDate(new Date(2015, 6, 15));

        var $element = $compile('<logs-date-filter></logs-date-filter>')($rootScope);
        $rootScope.$digest();

        console.log();

        expect($element.find('.btn').eq(4).html()).toContain('This month');
        expect($element.find('.btn').eq(3).html()).toContain('June');
        expect($element.find('.btn').eq(2).html()).toContain('May');
    });

});



