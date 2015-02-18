var editProfile = angular.module('editProfile', []);


// Controllers
editProfile.controller('profileController', function ($scope, $http) {
    $scope.formData = {};

    $scope.updateProfile = function() {
        $('#profile').css('opacity', '0.07');
        $('#loader').show();

        // console.log($scope.formData);

        $http.post('/profile', {
            'data': $scope.formData
        })
        .success(function(data) {
            if (data['error']) {
                $('#error_msg > .message').empty().append(data['error']);
                $('#error_msg').show();
            }

            if (data['success']) {
                $('#success_msg > .message').empty().append(data['success']);
                $('#success_msg').show();

                setTimeout('window.location.replace("/");', 2200);
            }
        })
        .error(function(data) {
            // console.log(data);
            $('.error_msg#log > .message').empty().append('<strong>Error: </strong> An error occured while trying to save your article. Please try again.');
            $('.error_msg#log').show();
        });
    };
});
