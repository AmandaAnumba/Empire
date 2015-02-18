var dashboard = angular.module('dashboard', []);

// Directives


// Controllers
dashboard.controller('morphsearch', function ($scope, $http) {
    $scope.input = "";

    $scope.submitSearch = function() {
        // console.log($scope.input);

        $http.post('/search', {
            'searchTerm': $scope.input
        })
        .success(function(data) {
            if (data['error']) {
                $('.error_msg#log > .message').empty().append(data['error']);
                $('.error_msg#log').show();
            }

            if (data['data']) {
                console.log(data['data']);
                $('#columnCategories').hide();
                $('#searchResults').empty().show();
            }

            if (data['nodata']) {
                console.log(data['nodata']);
            }
        })
        .error(function(data) {
            // console.log(data);
            $('.error_msg#log > .message').empty().append("<strong>Error: </strong>Please refresh the page and try again.");
            $('.error_msg#log').show();
        });
    };
});

