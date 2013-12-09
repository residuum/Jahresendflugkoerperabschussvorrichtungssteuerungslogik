// Copyright (c) 2012-2013 Thomas Mayer <thomas@residuum.org>
// 
// Permission is hereby granted, free of charge, to any person obtaining a
// copy of this software and associated documentation files (the "Software"),
// to deal in the Software without restriction, including without limitation
// the rights to use, copy, modify, merge, publish, distribute, sublicense,
// and/or sell copies of the Software, and to permit persons to whom the
// Software is furnished to do so, subject to the following conditions:
// 
// The above copyright notice and this permission notice shall be included
// in all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
// EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
// MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
// NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
// DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
// OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR
// THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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
		});
		for(var i = 0; i < $scope.pins.length; i++) {
			if ($scope.pins[i].no === pinNo) {
				$scope.pins[i].status = false;
				break;
			}
		}
	};

	$interval(function(){
		$scope.getStati()
	}, 2000, 0, true);
	
	$scope.getStati();
});
