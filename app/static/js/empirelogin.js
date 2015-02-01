function empirelogin() {
    $('#login-form').hide();
    $('#loader').show();
    
    $.post('/login', {
    	username: $('#login-form input[name=username]').val(),
        password: $('#login-form input[name=password]').val()
    }).done(function(message) {
    	$('#loader').hide();

    	if (message['error']) {
        	$('#login_error #message').empty().append(message['error']);
        	$('#login_error, #login-form').show();
    	}

    	if (message['login']) {
        	$('#login_error #message').empty().append(message['login']);
        	$('#login_error, #login-form').show();
    	}

    	if (message['success']) {
    		console.log('success');
    		window.location = "/dashboard";
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
    
    var user = $('#register-form input[name=username]').val(),
    	pw = $('#register-form input[name=password]').val(),
    	confirm = $('#register-form input[name=confirm]').val(),
    	em = $('#register-form input[name=email]').val();

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


function reset() {
    $('#resetValform').hide();
    $('#loader').show();
    
    var pw = $('#resetValform input[name=password]').val(),
    	confirm = $('#resetValform input[name=confirm]').val(),
    	reset = $('#resetValform input[name=reset]').val(),
    	action = $('#resetValform input[name=actionType]').val();

	$.post('/check', {
        password: pw,
        confirm: confirm,
    	reset: reset,
    	actionType: action
    }).done(function(message) {
		$('#loader').hide();

    	if (message['password_invalid']) {
    		$('#resetValform').show();
        	$('#tt_match').addClass('in');
        	setTimeout('jQuery("#tt_match").removeClass("in");', 7000)
    	}

    	if (message['password']) {
    		$('#resetValform').show();
        	$('#tt_pw .tooltip-inner').empty().append(message['password']);
        	$('#tt_pw').addClass('in');
        	setTimeout('jQuery("#tt_pw").removeClass("in");', 7000)
    	}

    	if (message['success']) {
        	$('#alert_message #message').empty().append(message['success']);
    		$('#alert_message').addClass('success').show();
    		$('#return').show();
    	}

    	if (message['error']) {
    		$('#resetValform').show();
        	$('#alert_message #message').empty().append(message['error']);
    		$('#alert_message').addClass('error').show();
    		setTimeout('jQuery("#alert_message").hide();', 7000)
    	}
    }).fail(function() {
        $('#loader').hide();
        $('#alert_message #message').empty().append("<strong>Error: </strong>Please refresh the page and try again.");
    	$('#alert_message').addClass('error').show();
    }); 
}