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
            exp = new Date(response.authResponse.expiresIn).toISOString();

            // console.log(access_token, user_id);

            FB.api('/me', {fields:'first_name,last_name,cover,email'}, function(response) {
                email = response.email;
                first = response.first_name;
                last = response.last_name;
                pic = response.cover.source; 

                console.log(pic);

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
                        console.log('login error');
                    }
                    if (message['success']) {
                        var userData = {
                            "id": message['uID'],
                            "avatarUrl": message['avatar'],
                            "authorUrl": 'none',
                            "name": message['fullname'],
                            "sessionType": 'Facebook'
                        };
                        localStorage.setItem("currentUser", JSON.stringify(userData));
                        
                        if (message['status'] === '201 Created') {
                            window.location = "/profile";
                        }

                        if (message['status'] === '200 OK') {
                            window.location = "/";
                        }
                    }
                }).fail(function() {
                    $('#login_error #message').empty().append("<strong>Error: </strong>Please refresh the page and try again.");
                    $('#login_error').show();
                    console.log('fatal error');
                });         
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

function fblogout() {
    FB.logout(function(response) {
        console.log(response);
        location.reload();
    });    
}