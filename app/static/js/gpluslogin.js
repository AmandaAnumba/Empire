function onLoadCallback() {
    gapi.client.setApiKey('AIzaSyCAcGnEM5Szftq4U7DQ8_e5v4LyQ6hqbDo'); //set your API KEY
    gapi.client.load('plus', 'v1',function(){});//Load Google + API
}

function gpluslogin() {
    var myParams = {
        'clientid' : '778066252083-gupksmvg6280pc0u9cptlm1sc37v9srh.apps.googleusercontent.com', //You need to set client id
        'cookiepolicy' : 'single_host_origin',
        'callback' : 'loginCallback', //callback function
        'approvalprompt':'force',
        'scope' : 'https://www.googleapis.com/auth/plus.login https://www.googleapis.com/auth/plus.profile.emails.read'
    };
    gapi.auth.signIn(myParams);
}

function loginCallback(result) {
    if (result['status']['signed_in']) {
        var request = gapi.client.plus.people.get({
            'userId': 'me'
        });

        request.execute(function (resp) {
            var fullname = resp.displayName,
                email = resp.emails[0].value,
                avatar = resp.image.url,
                id = resp.id,

            console.log(resp);
        });
    }
}

function gpluslogout() {
    gapi.auth.signOut();
    location.reload();
}