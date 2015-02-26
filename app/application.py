from app import app
import sys, re, string, base64, hmac, urllib, json, httplib, datetime
# from emails import *
from flask import render_template, session, request, redirect, url_for, escape, jsonify
# from oauth import OAuthSignIn

application = app

reload(sys)
sys.setdefaultencoding("utf-8")


# Globals
# --------------
CURRCYCLE = 1

# Parse database connection for RESTful API calls
connection = httplib.HTTPSConnection('api.parse.com', 443)
PARSEappID = "ijqxeiardpj4GzolLOo2lhzegVopVBnn9bcHyIOs"
RESTapiKEY = "Rip5cgtxGNddTSe3yAoWdiIeJpMDALKJmUastpyf" 


@application.route('/')
def index():
    if session.get('username') and session.get('sessionToken') and session.get('uID'):
        
        # get the user's information
        connection.connect()
        connection.request('GET', '/1/users/me', '', {
            "X-Parse-Application-Id": PARSEappID,
            "X-Parse-REST-API-Key": RESTapiKEY,
            "X-Parse-Session-Token": escape(session['sessionToken'])
        })

        result = json.loads(connection.getresponse().read())
        # print result

        if 'error' in result.keys():
            return render_template('misc/index.html', username=None, loggedIn=False)

        if 'subscriptions' in result.keys():
            x = len(result['subscriptions'])
       	    return render_template('user/dash_user.html', username=escape(session['username']), user=result, subscriptions=x)

        else:
            return render_template('user/dash_user.html', username=escape(session['username']), user=result, subscriptions=0)

    else:
    	return render_template('misc/index.html', username=None, loggedIn=False)


@application.route('/login', methods=['POST'])
def login():
    post = json.loads(request.data)

    username = post['data']['username']
    password = post['data']['password']
    remember = post['data']['remember'] 

    params = urllib.urlencode({"username":username,"password":password})
    connection.connect()
    connection.request('GET', '/1/login?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })
    
    result = json.loads(connection.getresponse().read())
    
    if 'error' in result.keys():
        # ERROR: {u'code': 101, u'error': u'invalid login parameters'}
        return jsonify({'error': '<strong>Error:</strong> Your login information was incorrect. Please try again or ensure that you have an Empire account.'})
    
    else:
        session['username'] = result['username']
        session['sessionToken'] = result['sessionToken']
        session['sessionType'] = 'Empire'
        session['uID'] = result['objectId']
        
        # stay logged in longer
        if remember == True:
        	session.permanent = True
        else:
        	session.permanent = False

        return jsonify({ 
            'success': 'success',
            'username': result['username'],
            'sessionType': 'Empire',
            'uID': result['objectId'],
        })


@application.route('/fblogin', methods=['POST'])
def fblogin():
    name = request.form.get('name', None)
    email = request.form.get('email', None)
    avatar = request.form.get('avatar', None)
    token = request.form.get('token', None)
    expire = request.form.get('expire', None)
    uID = request.form.get('id', None)

    connection.connect()
    connection.request('POST', '/1/users', json.dumps({
        "fullname": name,
        "email": email,
        "avatar": avatar,
        "username": " ",
        "role": "Member",
        "authData": {
            "facebook": {
                "id": uID,
                "access_token": token,
                "expiration_date": expire,
            }
        }
    }), {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY,
        "Content-Type": "application/json"
    })
    result = json.loads(connection.getresponse().read())

    
    if 'error' in result.keys():
        print '\n', result, '\n'
        return jsonify({ 'error': "<strong>Error:</strong> There was a problem signing in with your Facebook account. Please try again."})
    
    else:
        print result 
        return ""
        # session['username'] = name
        # session['sessionToken'] = result['sessionToken']
        # session['sessionType'] = 'Facebook'
        # session['uID'] = result['objectId']

        # return jsonify({ 
        #     'success': 'success',
        #     'username': 'none',
        #     'fullname': name,
        #     'uID': result['objectId'],
        #     'avatar': avatar,
        #     'status': result['status']
        # })


# @application.route('/authorize/<provider>')
# def oauth_authorize(provider):
#     oauth = OAuthSignIn.get_provider(provider)
#     return oauth.authorize()


# @application.route('/callback/<provider>')
# def oauth_callback(provider):
#     print "hit target"
#     oauth = OAuthSignIn.get_provider(provider)
#     print "back"
#     social_id, username, email = oauth.callback()


@application.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    session.pop('sessionToken', None)
    session.pop('sessionType', None)
    session.pop('uID', None)
    return redirect(url_for('index'))


@application.route('/register', methods=['POST'])
def register():
    post = json.loads(request.data)

    username = post['register']['username']
    email = post['register']['email']
    password = post['register']['password']

    try:
        connection.connect()
        connection.request('POST', '/1/users', json.dumps({
            "username": username,
            "password": password,
            "email": email,
            "subscriptions": [],
            "followers": [],
            "following": [],
        }), {
            "X-Parse-Application-Id": PARSEappID,
            "X-Parse-REST-API-Key": RESTapiKEY,
            "Content-Type": "application/json"
        })
        
        result = json.loads(connection.getresponse().read())

        if 'error' in result.keys():
            print "error while registering"
            return jsonify({ 'error': "There was a problem while creating your account. Please try again." })

        else:
            session['username'] = username
            session['sessionToken'] = result['sessionToken']
            session['sessionType'] = 'Empire'
            session['uID'] = result['objectId']

            # stay logged in longer
            session.permanent = True

            return jsonify({ 'success': "Registration successful. You are now logged in." })

    except:
        return jsonify({ 'error': "There was a problem while creating your account. Please try again." })


@application.route('/forgot', methods=['POST'])
def forgot():
    post = json.loads(request.data)

    email = post['email'].lower()

    connection.connect()
    connection.request('POST', '/1/requestPasswordReset', json.dumps({
        "email": email
    }), {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY,
        "Content-Type": "application/json"
    })

    result = json.loads(connection.getresponse().read())

    if 'error' in result.keys():
        print "error"
        return jsonify({ 'error': "We cannot find the account associated with this email address. Please enter the email address used to register your account." })

    else:
        print 'success'
        return jsonify({ 'success': "An email has been sent to you. Please follow the link to reset your password." })


# ------------------------------------------------
# other pages
# ------------------------------------------------
@application.route('/home')
def home():
    if session.get('username') and session.get('sessionToken') and session.get('uID'):
        username = escape(session['username'])
        return render_template('misc/index.html', username=username, loggedIn=True)
    else:
        return render_template('misc/index.html', loggedIn=False)

@application.route('/about')
def about():
    return render_template('misc/about.html')

@application.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("misc/contact.html")

    elif request.method == 'POST':
        name = request.form.get('name', None)
        email = request.form.get('email', None)
        subject = request.form.get('subject', None)
        message = request.form.get('message', None)

        try:
            empireContact(name, email, subject, message)
            return jsonify({ 'success': "Your message has been sent. You will now be redirected to the front page." })

        except:
            return jsonify({ 'error': "Your email could not be sent. Please refresh the page and try again." })
    
@application.route('/terms')
def terms():
    return render_template("misc/terms.html")

@application.route('/privacy')
def privacy():
    return render_template("misc/privacy.html")