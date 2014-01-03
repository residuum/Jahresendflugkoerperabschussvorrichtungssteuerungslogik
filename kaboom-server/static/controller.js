'use strict'

var kaboomApp = angular.module('kaboomApp', []);

kaboomApp.controller('kaboom', function($scope, $http, $interval) {
	$scope.availTimes = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25];
	$scope.time = 10;
	$scope.pins = [];
	$scope.getStati = function() {
		$http.get('/status').success(function(data) {
			$scope.pins = data;
		});
	};
	$scope.shoot = function(pinNo) {
		$http.post('/shoot', {
			pin: pinNo, 
			time: $scope.time
		}).success(function(data) {
			for(var i = 0; i < $scope.pins.length; i++) {
				if ($scope.pins[i].no === pinNo) {
					$scope.pins[i].status = false;
					break;
				}
			}

		});
		for(var i = 0; i < $scope.pins.length; i++) {
			if ($scope.pins[i].no === pinNo) {
				$scope.pins[i].status = true;
				break;
			}
		}
	};

	/*	$interval(function(){
		$scope.getStati()
		}, 2000, 0, true);*/

	$scope.getStati();
});
