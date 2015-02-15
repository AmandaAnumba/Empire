window.fbAsyncInit = function() {
    FB.init({
        appId   : '345241442325838',
        oauth   : true,
        status  : true, // check login status
        cookie  : true, // enable cookies to allow the server to access the session
        xfbml   : true, // parse XFBML
        version : 'v2.2'
    });
};

(function(d, s, id){
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {return;}
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));

var user_pic;

function fb_login(){
    FB.login(function(response) {
        if (response.authResponse) {
            access_token = response.authResponse.accessToken;
            user_id = response.authResponse.userID;
            exp = response.authResponse.expiresIn;

            // console.log(access_token, user_id);

            FB.api('/me', {fields:'first_name,last_name,cover,email'}, function(response) {
                email = response.email;
                first = response.first_name;
                last = response.last_name;
                pic = response.cover.source; 

                // console.log(first, last, pic, email);

                // post data to Parse DB
                $.post('/fblogin', {
                    name: first + ' ' + last,
                    email: email,
                    avatar: pic,
                    token: access_token,
                    id: user_id,
                    expire: exp
                }).done(function(message) {
                    if (message['error']) {
                        $('#login_error #message').empty().append(message['error']);
                        $('#login_error, #login-form').show();
                        console.log('error');
                    }

                    if (message['success']) {
                        window.location = "/dashboard";
                    }
                }).fail(function() {
                    $('#login_error #message').empty().append("<strong>Error: </strong>Please refresh the page and try again.");
                    $('#login_error').show();
                    console.log('error');
                });





                // var str2 = "<img style='width:50px;height:50px;margin-right:10px;' src='" + user_pic + "' /> ";
                // str2+= document.getElementById("mainusername").innerHTML;
                // str2+="<span style='color:#e64c65'>" + user_firstname + " " + user_lastname + "</span>";
                // str2+="<p id='fblogoutbtn' onclick='fblogout()' value='Logout' class='btn logout_btn'>Logout</p>";
                // document.getElementById("mainusername").innerHTML = str2

                // document.getElementById("fblogoutbtn").style.display = "block";
                // jQuery('#login').modal('hide');
                // document.getElementById("mainusername").style.display = "block";
                // document.getElementById("mainloginbtn").style.display = "none";
                // document.getElementById("mainregisterbtn").style.display = "none";           
            });
        } 
        else {
            //user hit cancel button
            console.log('User cancelled login or did not fully authorize.');
        }
    }, 
    {
        scope: 'public_profile,email,user_friends'
    });
}

function fblogout(){
  FB.logout(function(response) {
    console.log(response);
    location.reload();
  });    
}