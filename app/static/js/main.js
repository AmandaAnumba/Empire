$(document).ready(function() {
	$(".side-left > .intro-content").click(function(){
        $(this).find(".title").hide();

        $('#beta, #logo').hide();

        $("#categories").show().css('opacity', '1');

        $(".side-right").css({'width':'30%'});

        $(".side-left").css({'width':'70%', 'overflow-y': 'scroll'});

        // $("#logo").css({'left':'70%'});
    });

    $('#close_cat').click(function() {
    	$('.side-left > .intro-content').find(".title").show();

        $("#categories").show().css('opacity', '0').hide();

        $(".side-right").css({'width':'50%'});

        $(".side-left").css({'width':'50%', 'overflow-y': 'hidden'});

        $('#beta, #logo').show();

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
    // $(".side-left > .intro-content").mouseleave(function(){
    // 	$(this).find(".title").stop(true).delay(100).animate({
    //         opacity: 1
    //     }, 200);
    //     // $('#categories').hide();
    //     $("#categories").stop(true).delay(100).animate({
    //         opacity: 0,
    //         // top: 0
    //     }, 200);
    // });
	
	// $('#current_cycle').click(function() {
	// 	$('.container').css('opacity','0.2');
	// 	$('#loader').show();
	// });

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
	// $(document).click(function() {
	// 	$('.dropdown-menu').hide();
	// 	// if ($('.dropdown-menu').is(':visible')) {
	// 	// }
	// });

	// login/logout page buttons
	$('.btn-toggle').click(function() {
		// remove the active button if it's on anything else
		// $('.btn-toggle').not($(this)).removeClass('active');
		// $('.form').not('#'+$(this).attr('data-toggle')).hide();
		$('.panel').hide();

		// activate this specific form
		// $(this).addClass('active');
		var target = $(this).attr('data-toggle');
		$('#'+target).slideDown();

		// if (target == "register-form") {
		// 	$('.text-right').hide();
		// }
	});

});

function send() {
    // $('#about_wrapper form').css({'opacity':'0.2'});
    $('#about_wrapper form').hide();
    $('#loader').show();
    
    var name = $('#name').val(),
    	email = $('#email').val(),
    	subject = $('#subject').val(),
    	msg = $('textarea[name=message]').val();

    $.post('/contact', {
    	name: name,
        email: email,
        subject: subject,
        msg: msg
    }).done(function(message) {
    	$('#loader').hide();

    	if (message['error']) {
        	$('#error > .message').empty().append(message['error']);
        	$('#error, #about_wrapper > form').show();
    	}

    	if (message['success']) {
    		$('#success > .message').empty().append(message['success']);
        	$('#success').show();
        	setTimeout('window.location = "/";', 4000);
    	}

    }).fail(function() {
        $('#loader').hide();
        $('#error > .message').empty().append("<strong>Error: </strong>Please refresh the page and try again.");
        $('#error').show();
    });
}

function rate(action) {
    console.log('here');

    $.post('/rate', {
        id: $('#id').text(),
        action: action
    }).done(function(message) {

        if (message['error']) {
            console.log('error');
        }

        if (message['success']) {
            $('.smilie').hide();
            $('#message').show();
        }

    }).fail(function() {
        console.log('fail');
    });
}


// $(function() {
// 	<!-- initialize the slider -->
//     $('.slider').unslider({
//         speed: 600,
//         delay: 8000,
//         keys: false,
//         dots: true,
//         fluid: true
//     });

//     var win = $(window),
//         offset = 500;
    
//     win.scroll(function() {
//         if (win.scrollTop() >= offset) {
//             $('.header_navbar').addClass("fixed");
//             $('.header_navbar').css('margin-top','0');
//         } 
//         else {
//             $('.header_navbar').removeClass("fixed");
//             $('.header_navbar').css('margin-top','0px');
//         }
//     });

//     var shrinkHeader = 155;
//     $(window).scroll(function() {
//         var scroll = getCurrentScroll();
//         if ( scroll >= shrinkHeader ) {
//            $('.header').addClass('shrink');
//         }
//         else {
//             $('.header').removeClass('shrink');
//         }
//     });

//     function getCurrentScroll() {
//         return window.pageYOffset || document.documentElement.scrollTop;
//     }

//     // for the navbar
//     $('.menu_item').mouseenter( function() {
//         if ($(this).children().length > 1) {
//             $(this).addClass('open');
//             // $('.header')[0].style.height = (147 + $(this).find('.submenu')[0].offsetHeight) + 'px';
//             $(this).find('.submenu').css('visibility', 'visible');
//         }
//     });

//     $('.menu_item').mouseleave( function() {
//         if ($(this).children().length > 1) {
//             $(this).removeClass('open');
//             // $('.header')[0].style.height = '147px';
//             $(this).find('.submenu').css('visibility', 'hidden');
//         }
//     });
// });