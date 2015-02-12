var loginApp = angular.module('frontpage', []);

loginApp.controller('empirelogin', function ($scope) {
    $scope.phones = [
    {'name': 'Nexus S',
    'snippet': 'Fast just got faster with Nexus S.'},
    {'name': 'Motorola XOOM™ with Wi-Fi',
    'snippet': 'The Next, Next Generation tablet.'},
    {'name': 'MOTOROLA XOOM™',
    'snippet': 'The Next, Next Generation tablet.'}
    ];
});



function login() {
    $.post('/login', {
    	username: $('#main_login_form input[id=username]').val(),
        password: $('#main_login_form input[id=password]').val(),
        remember: $('#main_login_form input[id=remember]').val()
    }).done(function(message) {

    	if (message['error']) {
            console.log('error');
        	$('#login_error #message').empty().append(message['error']);
        	$('#login_error, #main_login_form').show();
    	}

    	if (message['login']) {
            console.log('error2');
        	$('#login_error #message').empty().append(message['login']);
        	$('#login_error, #main_login_form').show();
    	}

    	if (message['username']) {
    		console.log('username');
            
    		//var str2 = "<img style='width:50px;height:50px;margin-right:10px;' src='" + resp['image']['url'] + "' /> ";
            //str2+= document.getElementById("mainusername").innerHTML;
            var str2 = "Welcome ";
            str2+="<span style='color:#e64c65'>" + message['username'] + "</span>";
            str2+="<a id='empirelogoutbtn' class='btn logout_btn' href='{{ url_for('logout') }}'>Logout</a>";
            document.getElementById("mainusername2").innerHTML = str2;

            jQuery('#login').modal('hide');
            jQuery('#mainusername2').show();
            jQuery('empirelogoutbtn').show();
            document.getElementById("mainusername2").style.display = "block";
            document.getElementById("mainloginbtn").style.display = "none";
            document.getElementById("mainregisterbtn").style.display = "none";
    	}

    }).fail(function() {
        $('#loader').hide();
        $('#login_error #message').empty().append("<strong>Error: </strong>Please refresh the page and try again.");
        $('#login_error').show();
    });
}

function empireregister() {
    $('#register-form').hide();
    $('#loader').show();
    
    var user = $('#main_register_form input[name=username]').val(),
    	pw = $('#main_register_form input[name=password]').val(),
    	confirm = $('#main_register_form input[name=confirm]').val(),
    	em = $('#main_register_form input[name=email]').val();

    console.log(em);
    
	$.post('/register', {
    	username: user,
        email: em,
        password: pw,
        confirm: confirm
    }).done(function(message) {
    	$('#register-form').show();
		$('#loader').hide();

    	if (message['user']) {
        	$('#tt_us').addClass('in');
        	setTimeout('jQuery("#tt_us").removeClass("in");', 7000);
    	}

    	if ((message['email']) && (message['email'] == "exists")) {
        	$('#tt_em1').addClass('in');
        	setTimeout('jQuery("#tt_em1").removeClass("in");', 7000);
    	}

    	if ((message['email']) && (message['email'] == "invalid")) {
        	$('#tt_em2').addClass('in');
        	setTimeout('jQuery("#tt_em2").removeClass("in");', 7000);
    	}

    	if (message['password-invalid']) {
        	$('#tt_pw').addClass('in');
        	setTimeout('jQuery("#tt_pw").removeClass("in");', 7000);
    	}

    	if (message['password']) {
        	$('#tt_pw2 .tooltip-inner').empty().append(message['password']);
        	$('#tt_pw2').addClass('in');
        	setTimeout('jQuery("#tt_pw2").removeClass("in");', 7000);
    	}

    	if (message['error']) {
        	$('#reg_error #message').empty().append(message['error']);
    		$('#reg_error').show();
    		setTimeout('jQuery("#reg_error").hide();', 5500);
    	}

    	if (message['success']) {
        	$('#register-form').hide();
        	$('#reg_success #message').empty().append(message['success']);
    		$('#reg_success').show();
    		setTimeout('jQuery("#reg_success").hide();', 2700);
    		setTimeout('window.location.replace("/");', 2700);
    	}
    }).fail(function() {
        $('#loader').hide();
        $('#reg_error #message').empty().append("<strong>Error: </strong>Please refresh the page and try again.");
        $('#reg_error').show();
    }); 
}


function forgotPass() {
    $('#forgot-form').hide();
    $('#loader').show();
    
    var em = $('#forgot-form input[name=email]').val();

	$.post('/forgot', {
        email: em
    }).done(function(message) {
		$('#loader').hide();

    	if (message['success']) {
        	$('#forgot_error #message').empty().append(message['success']);
    		
    		if ($('#forgot_error').hasClass('error')) {
    			$('#forgot_error').removeClass('error').addClass('success').show();
    		}
    		else {
    			$('#forgot_error').addClass('success').show();
    		}
    	}

    	if (message['error']) {
        	$('#forgot_error #message').empty().append(message['error']);
    		$('#forgot-form').show();

    		if ($('#forgot_error').hasClass('success')) {
    			$('#forgot_error').removeClass('success').addClass('error').show();
    		}
    		else {
    			$('#forgot_error').addClass('error').show();
    		}
    	}
    }).fail(function() {
        $('#loader').hide();
        $('#forgot_error #message').empty().append("<strong>Error: </strong>Please refresh the page and try again.");
    	$('#forgot_error').addClass('error').show();
    }); 
}
