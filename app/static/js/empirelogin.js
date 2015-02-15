var index = angular.module('index', [])
    .directive('pwCheck', [function () {
        return {
            require: 'ngModel',
            link: function (scope, elem, attrs, ctrl) {
                var firstPassword = '#' + attrs.pwCheck;
                elem.add(firstPassword).on('keyup', function () {
                    scope.$apply(function () {
                        var v = elem.val()===$(firstPassword).val();
                        ctrl.$setValidity('pwmatch', v);
                    });
                });
            }
        }
    }]);

index.controller('loginFormController', function ($scope, $http) {
    // create a blank object to hold our form information
    // $scope will allow this to pass between controller and view
    $scope.formData = {};
    // console.log($scope.formData);

    // process the form
    $scope.login = function() {
        // console.log($scope.formData);

        $http.post('/login', {
            'data': $scope.formData
        })
        .success(function(data) {
            // this callback will be called asynchronously
            // when the response is available
            console.log(data);

            if (data['error']) {
                $('#login_error #message').empty().append(data['error']);
                $('#login_error, #main_login_form').show();
            }

            if (data['success']) {
                window.location = "/myhome";
            }
        })
        .error(function(data) {
            // called asynchronously if an error occurs
            // or server returns response with an error status.
            console.log(data);
            // $('#loader').hide();
            // $('#login_error #message').empty().append("<strong>Error: </strong>Please refresh the page and try again.");
            // $('#login_error').show();
        });
    };
});

index.controller('registerFormController', function ($scope, $http) {

    $scope.formData = {};
    $scope.register = function() {
        console.log($scope.formData);

        $http.post('/register', {
            'data': $scope.formData
        })
        .success(function(data) {
            console.log(data);

            if (data['error']) {
                $('.error_msg#reg > .message').empty().append(data['error']);
                $('.error_msg#reg').show();
            }

            if (data['success']) {
                // prompt them to fill out their profile; simple profile
                // - show full name
                // - show email
                // - show avatar
                // - add their social media info
                window.location = "/myhome";
            }
        })
        .error(function(data) {
            console.log(data);
            $('.error_msg#reg > .message').empty().append("<strong>Error: </strong>Please refresh the page and try again.");
            $('.error_msg#reg').show();
        });
    };
});

index.controller('forgotFormController', function ($scope, $http) {
    $scope.formData = {};
    $scope.forgot = function() {
        console.log($scope.formData.email);

        $http.post('/forgot', {
            'email': $scope.formData.email
        })
        .success(function(data) {
            // this callback will be called asynchronously
            // when the response is available
            console.log(data);

            if (data['error']) {
                $('.error_msg.forgot > .message').empty().append(data['error']);
                $('.error_msg.forgot').show();
            }

            if (data['success']) {
                $('.success_msg.forgot > .message').empty().append(data['success']);
                $('.success_msg.forgot').show();
            }
        })
        .error(function(data) {
            // called asynchronously if an error occurs
            // or server returns response with an error status.
            $('.error_msg.forgot > .message').empty().append("<strong>Error: </strong>Please refresh the page and try again.");
            $('.error_msg.forgot').show();
        });
    };
});
