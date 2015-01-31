
function onLoadCallback()
{
    gapi.client.setApiKey('AIzaSyCAcGnEM5Szftq4U7DQ8_e5v4LyQ6hqbDo'); //set your API KEY
    gapi.client.load('plus', 'v1',function(){});//Load Google + API
}

function gpluslogin() 
{
  var myParams = {
    'clientid' : '778066252083-gupksmvg6280pc0u9cptlm1sc37v9srh.apps.googleusercontent.com', //You need to set client id
    'cookiepolicy' : 'single_host_origin',
    'callback' : 'loginCallback', //callback function
    'approvalprompt':'force',
    'scope' : 'https://www.googleapis.com/auth/plus.login https://www.googleapis.com/auth/plus.profile.emails.read'
  };
  gapi.auth.signIn(myParams);
}




function loginCallback(result)
{
    if(result['status']['signed_in'])
    {
        var request = gapi.client.plus.people.get(
        {
            'userId': 'me'
        });
        request.execute(function (resp)
        {
            var email = '';
            if(resp['emails'])
            {
                for(i = 0; i < resp['emails'].length; i++)
                {
                    if(resp['emails'][i]['type'] == 'account')
                    {
                        email = resp['emails'][i]['value'];
                    }
                }
            }
 
            /**var str = "Name: " + resp['displayName'] + "<br>";
            str += "Email: " + email + "<br>";
            str += "<img style='width:50px;height:50px;' src='" + resp['image']['url'] + "' /><br>";
            document.getElementById("profile").innerHTML = str;**/
          
          var str2 = "<img style='width:50px;height:50px;margin-right:10px;' src='" + resp['image']['url'] + "' /> ";
          str2+= document.getElementById("mainusername").innerHTML;
          str2+="<span style='color:#e64c65'>" + resp['displayName'] + "</span>";
          str2+="<p id='gpluslogoutbtn' onclick='gpluslogout()' value='Logout' class='btn logout_btn'>Logout</p>";
          document.getElementById("mainusername").innerHTML = str2

            document.getElementById("gpluslogoutbtn").style.display = "block";
            jQuery('#login').modal('hide');
            document.getElementById("mainusername").style.display = "block";
            document.getElementById("mainloginbtn").style.display = "none";
            document.getElementById("mainregisterbtn").style.display = "none";
        });
 
    }
 
}

function gpluslogout()
{
    gapi.auth.signOut();
    location.reload();
}