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
            console.log('Welcome!  Fetching your information.... ');
            //console.log(response); // dump complete info
            access_token = response.authResponse.accessToken; //get access token
            user_id = response.authResponse.userID; //get FB UID

            FB.api('/me', {fields:'first_name, last_name, cover,email'}, function(response) {
                user_email = response.email; //get users email
                //console.log(user_email);
                firstname = response.first_name; //get users first name
                lastname = response.last_name; //get users last name
                pic = response.cover.source; //get users profile picture
                //console.log(user_pic);
                // you can store this data into your database 
                console.log(firstname, lastname, pic, email);

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

(function() {
    //var e = document.createElement('script');
    //e.src = document.location.protocol + '//connect.facebook.net/en_US/all.js';
    //e.async = true;
    //document.getElementById('fb-root').appendChild(e);
}());

function fblogout(){
  FB.logout(function(response) {
    console.log(response);
    location.reload();
  });    
}