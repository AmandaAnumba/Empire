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
var user_pic;
function fb_login(){
    FB.login(function(response) {

        if (response.authResponse) {
            console.log('Welcome!  Fetching your information.... ');
            //console.log(response); // dump complete info
            access_token = response.authResponse.accessToken; //get access token
            user_id = response.authResponse.userID; //get FB UID

            FB.api('/me', function(response) {
                user_email = response.email; //get users email
                console.log(user_email);
                user_name = response.firt_name; //get users first name
                console.log(user_name);
                user_pic = response.picture; //get users profile picture
                console.log(user_pic);
          // you can store this data into your database 

          /**var str2 = "<img style='width:50px;height:50px;margin-right:10px;' src='" + user_pic + "' /> ";
          str2+= document.getElementById("mainusername").innerHTML;
          str2+="<span style='color:#e64c65'>" + user_name + "</span>";
          str2+="<p id='fblogoutbtn' onclick='fblogout()' value='Logout' class='btn logout_btn'>Logout</p>";
          document.getElementById("mainusername").innerHTML = str2

          document.getElementById("fblogoutbtn").style.display = "block";
          jQuery('#login').modal('hide');
          document.getElementById("mainusername").style.display = "block";
          document.getElementById("mainloginbtn").style.display = "none";
          document.getElementById("mainregisterbtn").style.display = "none";**/            
            });

        } else {
            //user hit cancel button
            console.log('User cancelled login or did not fully authorize.');

        }
    }, {
        scope: 'publish_stream,email,first_name,picture'
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
    location.reload();
  });    
}

// // This is called with the results from FB.getLoginStatus().
  // function statusChangeCallback(response) {
  //   console.log('statusChangeCallback');
  //   console.log(response);
  //   // The response object is returned with a status field that lets the
  //   // app know the current login status of the person.
  //   // Full docs on the response object can be found in the documentation
  //   // for FB.getLoginStatus().
  //   if (response.status === 'connected') {
  //     // Logged into your app and Facebook.
  //     testAPI();
  //   } else if (response.status === 'not_authorized') {
  //     // The person is logged into Facebook, but not your app.
  //     document.getElementById('status').innerHTML = 'Please log ' +
  //       'into this app.';
  //   } else {
  //     // The person is not logged into Facebook, so we're not sure if
  //     // they are logged into this app or not.
  //     document.getElementById('status').innerHTML = 'Please log ' +
  //       'into Facebook.';
  //   }
  // }

  // // This function is called when someone finishes with the Login
  // // Button.  See the onlogin handler attached to it in the sample
  // // code below.
  // function checkLoginState() {
  //   FB.getLoginStatus(function(response) {
  //     statusChangeCallback(response);
  //   });
  // }

  // window.fbAsyncInit = function() {
  // FB.init({
  //   appId      : '345241442325838',
  //   cookie     : true,  // enable cookies to allow the server to access 
  //                       // the session
  //   xfbml      : true,  // parse social plugins on this page
  //   version    : 'v2.2' // use version 2.2
  // });

  // // Now that we've initialized the JavaScript SDK, we call 
  // // FB.getLoginStatus().  This function gets the state of the
  // // person visiting this page and can return one of three states to
  // // the callback you provide.  They can be:
  // //
  // // 1. Logged into your app ('connected')
  // // 2. Logged into Facebook, but not your app ('not_authorized')
  // // 3. Not logged into Facebook and can't tell if they are logged into
  // //    your app or not.
  // //
  // // These three cases are handled in the callback function.

  // FB.getLoginStatus(function(response) {
  //   statusChangeCallback(response);
  // });

  // };

  // // Load the SDK asynchronously
  // (function(d, s, id) {
  //   var js, fjs = d.getElementsByTagName(s)[0];
  //   if (d.getElementById(id)) return;
  //   js = d.createElement(s); js.id = id;
  //   js.src = "//connect.facebook.net/en_US/sdk.js";
  //   fjs.parentNode.insertBefore(js, fjs);
  // }(document, 'script', 'facebook-jssdk'));

  // // Here we run a very simple test of the Graph API after login is
  // // successful.  See statusChangeCallback() for when this call is made.
  // function testAPI() {
  //   console.log('Welcome!  Fetching your information.... ');
  //   FB.api('/me', function(response) {
  //     console.log('Successful login for: ' + response.name);
  //     document.getElementById('status').innerHTML =
  //       'Thanks for logging in, ' + response.name + '!';
  //   });
  // }