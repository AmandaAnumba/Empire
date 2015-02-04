$(function() {
	
    $('.slim').slimScroll();
    $('.slim-lg').slimScroll({
        height: '500px'
    });
    
	$('#register-form input').hover(
		function() {
			var target = $(this).attr('help-text');
			$('#'+target).show();
		}, 
		function() {
			var target = $(this).attr('help-text');
			$('#'+target).hide();
		}
	);
});	


function empireregister() {
    //$('#register').hide();
        
    var user = $('#register input[name=username]').val(),
    	pw = $('#register input[name=password]').val(),
    	confirm = $('#register input[name=confirm]').val(),
    	em = $('#register input[name=email]').val();

	$.post('/register', {
    	username: user,
        email: em,
        password: pw,
        confirm: confirm
    }).done(function(message) {
    	//$('#register-form').show();

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