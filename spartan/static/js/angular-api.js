var app = angular.module('spartan', []);

var my_app = angular.module('spartan').config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

app.controller('SpartanController', function($scope) {

	var expectFriendNames = function(expectedNames, key) {
		element.all(by.repeater(key + ' in produits').column(key)).then(function(arr) {
			arr.forEach(function(wd, i) {
				expect(wd.getText()).toMatch(expectedNames[i]);
			});
		});
	};

});