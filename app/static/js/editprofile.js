var editProfile = angular.module('editProfile', []);


// Controllers
editProfile.controller('profileController', function($scope, $http) {
    $scope.formData = {};

    $scope.updateProfile = function() {
        $('#submitBtn').hide();
        $('#loader').show();

        console.log($scope.formData);

        // $http.post('/profile', {
        //     'data': $scope.formData
        // })
        // .success(function(data) {
        //     $('#loader').hide();

        //     if (data['error']) {
        //         console.log('saving error');
        //         $('#error_msg > .message').empty().append(data['error']);
        //         $('#error_msg').show();
        //     }

        //     if (data['success']) {
        //         $('#success_msg > .message').empty().append(data['success']);
        //         $('#success_msg').show();

        //         setTimeout('window.location.replace("/");', 2200);
        //     }
        // })
        // .error(function(data) {
        //     console.log('fatal error');
        //     $('.error_msg#log > .message').empty().append('<strong>Error: </strong> An error occured while trying to save your article. Please try again.');
        //     $('.error_msg#log').show();
        // });
    };
});
