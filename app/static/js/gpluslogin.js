
function onLoadCallback()
{
    gapi.client.setApiKey('AIzaSyCAcGnEM5Szftq4U7DQ8_e5v4LyQ6hqbDo'); //set your API KEY
    gapi.client.load('plus', 'v1',function(){});//Load Google + API
}

function login() 
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
 
            var str = "Name: " + resp['displayName'] + "<br>";
            str += "Email: " + email + "<br>";
            str += "<img style='width:50px;height:50px;' src='" + resp['image']['url'] + "' /><br>";
            document.getElementById("profile").innerHTML = str;

            document.getElementById("gpluslogoutbtn").style.display = "block";
            document.getElementById("gplusloginbtn").style.display = "none";
        });
 
    }
 
}

function logout()
{
    gapi.auth.signOut();
    location.reload();
}