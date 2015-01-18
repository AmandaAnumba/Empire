/*
    Things to refactor

    - use js object to implement the save draft
    - establish jquery variables for the 
    - use ====
    - try and use logic to reduce if statements
    - replace $('#').onclick with function calls
        + maybe replace with callback functions
    - create a draft management file and establish an object with vars and 
        functions to be called on
    - make sure all classes and ids across admin_proof, draft, write docs are
        the same
    - cut down on repetitive function calling (s3_upload_v1, s3_uplod_v2....)
    - look into implementing node and angular
    - make functions more versatile to handle multiple functionalities
    - structure docuemtn for Immediately Invoked Function Expression
        (function () {
         // Do fun stuff​
         }
        )()

 */


$(function() {
	// $('#menu-toggle>.icon').click( function() {
	// 	$(this).toggleClass('active');
	// 	$(this).parent().toggleClass('closed');
	// 	$('.menu_lg_wrapper').toggleClass('open');
	// 	$('#menu-toggle > p').toggle();

	// 	if (!$(this).hasClass('active')) {
	// 		$(this).removeClass('icon-cross').addClass('icon-menu');
	// 		$('#write_wrapper').css('margin-left', '4.6%');
	// 	}
	// 	else{
	// 		$(this).removeClass('icon-menu').addClass('icon-cross');
	// 		$('#write_wrapper').css('margin-left', '25.6%');
	// 	}
	// });
	
    $('.slim').slimScroll();
    $('.slim-lg').slimScroll({
        height: '500px'
    });
    
	$('#menu-toggle').click(function() {
		var $icon = $(this).find('.icon'),
			$header = $('.menu_top_wrapper');

		if ($icon.hasClass('icon-maximize')) {
			$icon.removeClass('icon-maximize').addClass('icon-minimize');
		}

		else if ($icon.hasClass('icon-minimize')) {
			$icon.removeClass('icon-minimize').addClass('icon-maximize');
		}

		$header.toggleClass('open');
		// $('#data').toggleClass('active');
	});
	$('.tab').click(function() {
		$(this).addClass('active');
		$('.tab').not(this).removeClass('active');
		$('.tab-content').hide();
		var target = $(this).attr('data-toggle');
		$('#'+target).show();
	});
	$('button.close').click(function() {
        $(this).closest('.alert').hide();
    });
    $('button.panel-close').click(function() {
        $(this).closest('.panel').hide();
    });

	// login/logout page buttons
	$('.btn-toggle').click(function() {
		// remove the active button if it's on anything else
		// $('.btn-toggle').not($(this)).removeClass('active');
		// $('.form').not('#'+$(this).attr('data-toggle')).hide();
		$('.form').hide();

		// activate this specific form
		// $(this).addClass('active');
		var target = $(this).attr('data-toggle');
		$('#'+target).slideDown();

		// if (target == "register-form") {
		// 	$('.text-right').hide();
		// }
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

	// add tags to the list to be checked
	$('#add2list').click(function() {
		var x = $('input[name=taginput]').val();

		if (x == "" || x == " ") {
			$('input[name=taginput]').val("");
			return;
		}
		else {
			if (!$('#tags_list').is(":visible")) {
				$('#tags_list').show();
			}
			var tags = x.split(',');

			for (var i=0; i < tags.length; i++) {
				$('#tags_list').append('<p><span class="icon-circle-cross remove_tag" onclick="$(this).parent().hide();"></span>'+tags[i].trim()+'</p>');
			}
			$('input[name=taginput]').val("");
		}
	});

	// dropdown menus
	$('.dropdown-toggle').click(function(e) {
		var target = $(this).attr('dropdown-toggle');
		$('.dropdown-menu').not('#'+target).hide();
		
		if ($('#'+target).is(':visible')) {
			$('#'+target).hide();
		}
		else {
			e.stopPropagation();
			$('#'+target).show();
		}
	});

	$(document).click(function() {
		$('.dropdown-menu').hide();
		// if ($('.dropdown-menu').is(':visible')) {
		// }
	});
	$('#change_avatar').click(function() {
		$('#change_avatar, #old_avatar').hide();
		$('#avi').show();
	});

	$("#avatar, #headerIMG").change(function() {
		readURL(this);
	});

	$('#profile').click(function() {
		$(this).css('opacity', '0.3');
		$('#loader').show();
	});

	$('.slide_toggle').click(function() {
		var $popout = $(this).parent();
		
		$('.popout').not($popout).animate({right:'-360px'}, {queue: false, duration: 500}).removeClass('popped');

		if ($popout.hasClass("popped")) {
			$popout.animate({right:'-360px'}, {queue: false, duration: 500}).removeClass('popped');
			$('.slide_toggle').not(this).show();
		}
		
		else {
			$popout.animate({right:'0px'}, {queue: false, duration: 500}).addClass('popped');
			$('.slide_toggle').not(this).hide();
		}
	});
	$('.slide_toggle-left').click(function() {
		var $popout = $(this).parent();
		
		$('.popout-left').not($popout).animate({left:'-360px'}, {queue: false, duration: 500}).removeClass('popped');

		if ($popout.hasClass("popped")) {
			$popout.animate({left:'-360px'}, {queue: false, duration: 500}).removeClass('popped');
			$('.slide_toggle-left').not(this).show();
		}
		
		else {
			$popout.animate({left:'0px'}, {queue: false, duration: 500}).addClass('popped');
			$('.slide_toggle-left').not(this).hide();
		}
	});
	$('#add-author').click(function() {
		$(this).hide();
		$('#more-authors').show();
	});

	$('#upload_btn2').click(function() {
		var name = $('#featureIMG').get(0).files[0].name.replace(/ /g,'').replace(/[&\/\\#,+()$~%^'":*?<>{}]/g, ''),
			selector = 'featureIMG',
			title = "";

		if (name.length > 20) {
		    title = name.substring((name.length-20),name.length);
		}

		else {
			title = name;
		}

		s3_upload_v2(title, selector);
	});

	$('#upload_btn3').click(function() {
		var name = $('#allmedia').get(0).files[0].name.replace(/ /g,'').replace(/[&\/\\#,+()$~%^'":*?<>{}]/g, ''),
			selector = 'allmedia',
			title = "";

		if (name.length > 20) {
		    title = name.substring((name.length-20),name.length);
		}

		else {
			title = name;
		}

		s3_upload_v3(title, selector);
	});

	$('#uploadAvi').click(function() {
		var name = $('#avatar').get(0).files[0].name.replace(/ /g,'').replace(/[&\/\\#,+()$~%^'":*?<>{}]/g, ''),
			selector = 'avatar',
			title = "";

		if (name.length > 20) {
		    title = name.substring((name.length-20),name.length);
		}

		else {
			title = name;
		}

		s3_upload_v4(title, selector);
	});

	$('#finished').click(function() {
		var id 				= $('#id').text(),
			title           = $('input[name=title]').val(),
		    author          = $('input[name=author]').val(),
		    coAuthor        = $('input[name=co-author]').val(),
		    content         = $('#editor').editable('getHTML', false, true),
		    featureIMG      = $('input[name=featureIMGurl]').val(),
		    headerIMG       = $('input[name=headerIMGurl]').val(),
		    description     = $('textarea[name=description]').val(),
		    releaseDate     = $('input[name=release]').val(),
		    currRelease     = $('#rDate').text(),
		    currRelease2    = $('#releaseDate').text(),
		    doctype         = $('input[name=doctype]:checked').val(),
		    selected 		= [],
		    options 		= [],
		    release 		= "",
		    photoCred 		= "",
		    category 		= "",
		    tags 			= "",
		    photoCredOrig 	= $('#photo_cred_orig').val(),
		    photoCredNew 	= $('#photo_cred_new').val(),
		    currentCat 		= $('#current_cat').text(),
		    currentTags 	= $('#article_tags').text(),
		    catNew,
		    tagsNew,
		    counter = 0;

		// release date change
		if ((currRelease !== 'No date selected') && !releaseDate) {
			$('#fRelease').empty().append(currRelease);
			$('#dateForRelease').empty().append(currRelease2);
		}
		if ((currRelease === 'No date selected') && (releaseDate) ) {
			$('#fRelease').empty().append(moment(releaseDate).format("dddd, MMMM Do YYYY"));
			$('#dateForRelease').empty().append(moment(releaseDate).toArray().toString());
		}
		if (releaseDate) {
			$('#fRelease').empty().append(moment(releaseDate).format("dddd, MMMM Do YYYY"));
			$('#dateForRelease').empty().append(moment(releaseDate).toArray().toString());
		}
		if ((currRelease === 'No date selected') && (!releaseDate) ) {
			$('#fRelease').empty().append('<span class="icon icon-cross text-danger"></span> No Date Selected');
			$('#dateForRelease').empty().append('None');
			counter ++;
		}

		// title
		if (title) {
			$('#fTitle').empty().append(title);
		}
		if (!title) {
			$('#fTitle').empty().append('<span class="icon icon-cross text-danger"></span> No Title');
			counter ++;
		}

		// author
		$('#fAuthor').empty().append(author);

		// coAuthor
		if (!coAuthor) {
			$('#fCo').empty().append('None');
		}
		if (coAuthor) {
			$('#fCo').empty().append(coAuthor);
		}

		// type
		$('#fType').empty().append(doctype);

		// categories
		$('#category option:selected').each(function() {
			options.push($(this).val());
		});
		
		catNew = options.join(", ");
		
		if ((options.length === 0) && (currentCat)) {
			category = currentCat;
		}
		if (options.length !== 0) {
			category = catNew;
		}
		if ((options.length === 0) && (!currentCat)) {
			category = '<span class="icon icon-cross text-danger"></span> None';
			counter ++;
		}
		$('#fCategory').empty().append(category);

		// tags
		$('#tags_list p').each(function() {
			selected.push($(this).text());
		});
		
		tagsNew = selected.join(", ");

		if ((selected.length === 0) && (currentTags)) {
			tags = currentTags;
		}
		if (selected.length !== 0) {
			tags = tagsNew;
		}
		if ((selected.length === 0) && (!currentTags)) {
			tags = '<span class="icon icon-cross text-danger"></span> None';
			counter ++;
		}
        $('#fTags').empty().append(tags);


		if (!description) {
			$('#fDescription').empty().append('<span class="icon icon-cross text-danger"></span> None');
			counter ++;
		}
		if (description) {
			$('#fDescription').empty().append(description);
		}

        if (!content) {
            $('#fContent').empty().append('<span class="icon icon-cross text-danger"></span> No Article Written');
            counter ++;
        }
        if (content) {
            $('#fContent').empty().append('<span class="icon icon-check text-success"></span>');
        }

		if (!headerIMG) {
			$('#fHeader').empty().append('<span class="icon icon-cross text-danger"></span>');
			counter ++;
		}
		if (headerIMG) {
			$('#fHeader').empty().append('<span class="icon icon-check text-success"></span>');
		}

		if (!featureIMG) {
			$('#fFeature').empty().append('<span class="icon icon-cross text-danger"></span>');
			counter ++;
		}
		if (featureIMG) {
			$('#fFeature').empty().append('<span class="icon icon-check text-success"></span>');
		}

		// photo cred
        if (photoCredOrig && !photoCredNew ) {
			$('#fPhotoCred').empty().append(photoCredOrig);
		}
		if (!photoCredOrig && photoCredNew ) {
			$('#fPhotoCred').empty().append(photoCredNew);
		}
		if (!photoCredOrig  && !photoCredNew ) {
			$('#fPhotoCred').empty().append('<span class="icon icon-cross text-danger"></span> No Photo Cred Given <span style="font-style:italics;">(not needed>)</span>');
		}

		if (counter > 0) {
			$('#proofBTN').attr('disabled', 'disabled');
		}

		if (counter === 0) {
			$('#proofBTN').removeAttr('disabled');
		}
	});

    $('#change_img').click(function() {
        $(this).hide();
        $('#photo_cred_orig, #header_old').hide();
        $('#avi').show();
    });
});	

function catChange() {
	$('#catChange').hide();
	$('#category').show();
}


function changeIMG() {
	$('#fIMG, #changeIMG, #fIMG-des').hide();
	$('#change_image').show();
}


function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
			$('#pic_icon span').hide();
			$('#avatar_pic').attr('src', e.target.result).show();

			if ($(input).attr('name') == "headerIMG") {
        		$('#upload_btn1, #photo_cred, #photo_cred_new').show();
        		$('.response').hide();
			}
       
        }

        reader.readAsDataURL(input.files[0]);
    }
}


function login() {
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


function register() {
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


function val() {
    $('#resetValform').hide();
    $('#loader').show();
    
    var code = $('#resetValform input[name=code]').val(),
    	action = $('#resetValform input[name=actionType]').val();

	$.post('/check', {
        code: code,
    	actionType: action
    }).done(function(message) {
		$('#loader').hide();

    	if (message['success']) {
        	$('#alert_message #message').empty().append(message['success']);
    		$('#alert_message').addClass('success').show();
    		$('#return').show();
    	}

    	if (message['error']) {
    		$('#resetValform').show();
        	$('#alert_message #message').empty().append(message['error']);
    		$('#alert_message').addClass('error').show();
    	}
    }).fail(function() {
        $('#loader').hide();
        $('#alert_message #message').empty().append("<strong>Error: </strong>Please refresh the page and try again.");
    	$('#alert_message').addClass('error').show();
    }); 
}


function postArticle(action) {
	// $('#register-form').hide();
    // $('#loader').show();
    
    var title           = $('#post input[name=title]').val(),
	    author          = $('#post input[name=author]').val(),
	    description     = $('#post textarea[name=description]').val(),
	    content         = $('#editor').editable('getHTML', false, true),
	    featureIMG      = $('#post input[name=featureIMGurl]').val(),
	    releaseDate     = $('input[name=release]').val(),
	    doctype         = $('#post input[name=doctype]:checked').val(),
	    headerIMG       = $('#post input[name=headerIMGurl]').val(),
	    coAuthor        = $('#post input[name=co-author]').val(),
	    photoCred       = $('#post input[name=photo_cred]').val(),
	    selected = new Array(),
	    options = new Array(),
	    release = "";

	$('#tags_list p').each(function() {
		selected.push($(this).text());
	});
	var tags = selected.join(", ");

	$('#category option:selected').each(function() {
		options.push($(this).val());
	});
	var category = options.join(", ");

	if (title == "") {
		var date = moment().format("MM/D/YYYY");
		title = "Article "+ date;
	}

	if (releaseDate == "") {
		release = null;
	}

	if (releaseDate != "") {
		release = moment(releaseDate).toArray().toString();
	}

	$.post('/submit', {
    	title: title,
	    author: author,
	    description: description,  
	    content: content, 
	    featureIMG: featureIMG,
	    status: action,
	    releaseDate: release, 
	    doctype: doctype,  
	    headerIMG: headerIMG,    
	    coAuthor: coAuthor,      
	    tags: tags,
	    category: category,
	    photoCred: photoCred
    }).done(function(message) {
    	if (message['success']) {
        	$('#success_msg > .message').empty().append(message['success']);
        	$('#success_msg').show();
        	setTimeout('window.location = "/dashboard";', 3500);
    	}

    	if (message['error']) {
        	$('#error_msg > .message').empty().append(message['error']);
        	$('#error_msg').show();
    	}
    }).fail(function() {
    	$('#error_msg > .message').empty().append('<strong>Error: </strong> An error occured while trying to save your article. Please try again.');
    	$('#error_msg').show();
    }); 
}


function save(action) {
	var id 				= $('#id').text(),
		title           = $('input[name=title]').val(),
	    author          = $('input[name=author]').val(),
	    coAuthor        = $('input[name=co-author]').val(),
	    content         = $('#editor').editable('getHTML', false, true),
	    featureIMG      = $('input[name=featureIMGurl]').val(),
	    headerIMG       = $('input[name=headerIMGurl]').val(),
	    description     = $('textarea[name=description]').val(),
	    releaseDate     = $('input[name=release]').val(),
	    currRelease     = $('#rDate').text(),
	    doctype         = $('input[name=doctype]:checked').val(),
	    selected 		= [],
	    options 		= [],
	    release 		= "",
	    photoCred 		= "",
	    category 		= "",
	    currentCat 		= $('#current_cat').text(),
	    catNew;

	// release date change
	if ((currRelease !== 'No date selected') && !releaseDate) {
		release = $('#releaseDate').text();
	}
	if ((currRelease === 'No date selected') && (releaseDate !== "") ) {
		release = moment(releaseDate).toArray().toString();
	}
	if (releaseDate) {
		release = moment(releaseDate).toArray().toString();
	}
	if ((currRelease === 'No date selected') && (releaseDate === "") ) {
		release = 'None';
	}
	
	// title
	if (!title) {
		var date = moment().format("MM/D/YYYY");
		title = "Article "+ date;
	}

	// photo cred
	if (!$('#header_old').is(':visible')) {
	    photoCred = $('#post input[name=photo_cred_new]').val();	
	}
	if ($('#header_old').is(':visible')) {
	    photoCred = $('#post input[name=photo_cred_orig]').val();	
	}

	// categories
	$('#category option:selected').each(function() {
		options.push($(this).val());
	});
	
	catNew = options.join(", ");
	// console.log(catNew);
	
	if ((options.length === 0) && (currentCat)) {
		category = currentCat;
	}
	if (options.length !== 0) {
		category = catNew;
	}
	if ((options.length === 0) && (!currentCat)) {
		category = 'None';
	}

	// tags
	$('#tags_list p').each(function() {
		selected.push($(this).text());
	});
	var tags = selected.join(", ");

	$.post('/update', {
		id: id,
    	title: title,
	    author: author,
	    description: description,  
	    content: content, 
	    featureIMG: featureIMG,
	    status: action,
	    releaseDate: release, 
	    doctype: doctype,  
	    headerIMG: headerIMG,    
	    coAuthor: coAuthor,      
	    tags: tags,
	    category: category,
	    photoCred: photoCred
    }).done(function(message) {
    	if (message['success']) {
        	$('#success_msg > .message').empty().append(message['success']);
        	$('#success_msg').show();
        	setTimeout('window.location = "/dashboard";', 3500);
    	}

    	if (message['error']) {
        	$('#error_msg > .message').empty().append(message['error']);
        	$('#error_msg').show();
    	}
    }).fail(function() {
    	$('#error_msg > .message').empty().append('<strong>Error: </strong> An error occured while trying to save your article. Please try again.');
    	$('#error_msg').show();
    }); 
}


function proofed() {
	var id 				= $('#id').text(),
		title           = $('#fTitle').text(),
	    author          = $('#fAuthor').text(),
	    coAuthor        = $('#fCo').text(),
	    content         = $('#editor').editable('getHTML', false, true),
	    featureIMG      = $('input[name=featureIMGurl]').val(),
	    headerIMG       = $('input[name=headerIMGurl]').val(),
	    description     = $('#fDescription').text(),
	    releaseDate     = $('#dateForRelease').text(),
	    doctype         = $('#fType').text(),
	    photoCred 		= $('#fPhotoCred').text(),
	    tags 			= $('#fTags').text(),
	    category 		= $('#fCategory').text();

	$.post('/update', {
		id: id,
    	title: title,
	    author: author,
	    description: description,  
	    content: content, 
	    featureIMG: featureIMG,
	    status: 'proofed',
	    releaseDate: releaseDate, 
	    doctype: doctype,  
	    headerIMG: headerIMG,    
	    coAuthor: coAuthor,      
	    tags: tags,
	    category: category,
	    photoCred: photoCred
    }).done(function(message) {
    	$('#finishModal').modal('hide');

    	if (message['success']) {
        	$('#success_msg > .message').empty().append(message['success']);
        	$('#success_msg').show();
        	setTimeout('window.location = "/dashboard";', 3500);
    	}

    	if (message['error']) {
        	$('#error_msg > .message').empty().append(message['error']);
        	$('#error_msg').show();
    	}
    }).fail(function() {
    	$('#error_msg > .message').empty().append('<strong>Error: </strong> An error occured while trying to save your article. Please try again.');
    	$('#error_msg').show();
    }); 
}


function deletedraft() {
	var id = $('#id').text();

	$.post('/delete', {
    	id: id
    }).done(function(message) {
    	$('#deleteModal').modal('hide')
    	if (message['success']) {
        	$('#success_msg > .message').empty().append(message['success']);
        	$('#success_msg').show();
        	setTimeout('window.location = "/dashboard";', 2700);
    	}

    	if (message['error']) {
        	$('#error_msg > .message').empty().append(message['error']);
        	$('#error_msg').show();
    	}
    }).fail(function() {
    	$('#error_msg > .message').empty().append('<strong>Error: </strong> An error occured while trying to delete this article. Please refresh the page and try again.');
    	$('#error_msg').show();
    }); 
}


function s3_upload(filename, selector){
	var circle = new ProgressBar.Circle('#circle-progress', {
	    color: '#7266ba',
	    strokeWidth: 6
	});

	$('#upload_btn1').hide();
	$('#circle-progress').show();

	var title = filename.replace(/ /g,'').replace(/[&\/\\#,+()$~%^'":*?<>{}]/g, ''),
		fn = "";

	if (title.length > 20) {
	    fn = title.substring((title.length-20),title.length);
	}

	if (title.length < 20) {
		fn = title;
	}

    var s3upload = new S3Upload({
    	s3_object_name: fn,
        file_dom_selector: selector,
        s3_sign_put_url: '/uploads/',

        onProgress: function(percent, message) {
            console.log('Upload progress: ' + percent + '% ' + message);
            if (percent == 100) {
            	circle.animate(1);
            }

            else {
            	circle.set(percent*0.01);
            }
        },
        onFinishS3Put: function(url) {
            $('#circle-progress').hide();
            $('#success_upload').show();
            $('input[name=headerIMGurl]').val(url);
            console.log(url);
        },
        onError: function(status) {
            console.log('Upload error: ' + status);
            $('#error_upload').show();
        }
    });
}


function s3_upload_v2(filename, selector){
	var line = new ProgressBar.Line('#progress2', {
	    color: '#BBB0FF',
	    strokeWidth: 2
	});

	$('#upload_btn2, .response').hide();
	$('#progress2').show();

    var s3upload = new S3Upload({
    	s3_object_name: filename,
        file_dom_selector: selector,
        s3_sign_put_url: '/uploads/',

        onProgress: function(percent, message) {
            console.log('Upload progress: ' + percent + '% ' + message);
            if (percent == 100) {
            	line.animate(1);
            }

            else {
            	line.set(percent*0.01);
            }
        },
        onFinishS3Put: function(url) {
            $('#progress2').hide();
            $('#success_upload2').show();
            $('input[name=featureIMGurl]').val(url);

            // $('#pop_uploads').show();

            // if (!$('#pop_uploads').hasClass('popped')) {
            // 	$('#pop_uploads').animate({left:'0px'}, {queue: false, duration: 500}).addClass('popped');
            // }

        	// var image = "<img src='"+url+"' alt='Article Image' />";
        	// $('#pop_uploads').find('.popout_content').append('<p class="label">'+filename+'</p><input class="clear-input-small2" type="text" value="'+image+'" readonly>');
        },
        onError: function(status) {
            console.log('Upload error: ' + status);
            $('#error_upload2').show();
        }
    });
}


function s3_upload_v3(filename, selector){
	var line = new ProgressBar.Line('#progress3', {
	    color: '#BBB0FF',
	    strokeWidth: 2
	});

	$('#upload_btn3, .response').hide();
	$('#progress3').show();

    var s3upload = new S3Upload({
    	s3_object_name: filename,
        file_dom_selector: selector,
        s3_sign_put_url: '/uploads/',

        onProgress: function(percent, message) {
            console.log('Upload progress: ' + percent + '% ' + message);
            if (percent == 100) {
            	line.animate(1);
            }

            else {
            	line.set(percent*0.01);
            }
        },
        onFinishS3Put: function(url) {
            $('#progress3').hide();
            $('#success_upload3, #pop_uploads, #upload_btn3').show();
            $('#allmedia').val('');

            if (!$('#pop_uploads').hasClass('popped')) {
            	$('#pop_uploads').animate({left:'0px'}, {queue: false, duration: 500}).addClass('popped');
            }

        	var image = "<img src='"+url+"' alt='Article Image' />";
        	$('#pop_uploads').find('.popout_content').append('<p class="label">'+filename+'</p><input class="clear-input-small2" type="text" value="'+image+'" readonly>');
        },
        onError: function(status) {
            console.log('Upload error: ' + status);
            $('#error_upload3').show();
        }
    });
}


function s3_upload_v4(filename, selector){
	var line = new ProgressBar.Line('#progress', {
	    color: '#e64c65',
	    strokeWidth: 2
	});

	$('#uploadAvi, .response').hide();
	$('#progress').show();

    var s3upload = new S3Upload({
    	s3_object_name: filename,
        file_dom_selector: selector,
        s3_sign_put_url: '/uploads/',

        onProgress: function(percent, message) {
            console.log('Upload progress: ' + percent + '% ' + message);
            if (percent == 100) {
            	line.animate(1);
            }

            else {
            	line.set(percent*0.01);
            }
        },
        onFinishS3Put: function(url) {
            $('#progress').hide();
            $('#success_upload').show();
            $('#imageURL').empty().append(url);
        },
        onError: function(status) {
            console.log('Upload error: ' + status);
            $('#error_upload').show();
        }
    });
}


function updateProfile() {
	$('#profile').css('opacity', '0.07');
    $('#loader').show();
    
    var email 		= $('input[name=email]').val(),
        fullname 	= $('input[name=fullname]').val(),
        bio 		= $('input[name=bio]').val(),
        avatar 		= $('#imageURL').text(),
        // password 	= $('input[name=email]').val(),
        // confirm 	= $('input[name=email]').val(),
        website 	= $('input[name=website]').val(),
        facebook 	= $('input[name=facebook]').val(),
        tumblr 		= $('input[name=tumblr]').val(),
        pinterest 	= $('input[name=pinterest]').val(),
        linkedin 	= $('input[name=linkedin]').val(),
        instagram 	= $('input[name=instagram]').val(),
        twitter 	= $('input[name=twitter]').val();

	$.post('/profile', {
    	email: email,
	    fullname: fullname,
	    bio: bio,  
	    avatar: avatar, 
	    website: website,
	    facebook: facebook,
	    tumblr: tumblr, 
	    twitter: twitter, 
	    pinterest: pinterest, 
	    linkedin: linkedin, 
	    instagram: instagram, 
    }).done(function(message) {
    	$('#loader').hide();
		$('#profile').css('opacity', '1');

    	if (message['success']) {
        	$('#success_msg > .message').empty().append(message['success']);
        	$('#success_msg').show();
        	setTimeout('window.location = "/dashboard";', 3500);
    	}

    	if (message['error']) {
        	$('#error_msg > .message').empty().append(message['error']);
        	$('#error_msg').show();
    	}
    }).fail(function() {
    	$('#error_msg > .message').empty().append('<strong>Error: </strong> An error occured while trying to save your article. Please try again.');
    	$('#error_msg').show();
    }); 
}

// to implement

// function recovery() { }
