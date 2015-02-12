from app import app
import sys, re, string, base64, hmac, urllib, json, httplib
# from emails import *
from flask import flash, render_template, session, request, redirect, url_for, escape, jsonify

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
       	username = escape(session['username'])
       	return render_template('misc/index.html', username=username, loggedin=True)
    else:
    	return render_template('misc/index.html', username=None, loggedin=False)


@application.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', None)
    password = request.form.get('password', None)
    remember = request.form.get('remember', None)

    params = urllib.urlencode({"username":username,"password":password})
    connection.connect()
    connection.request('GET', '/1/login?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })
    
    result = json.loads(connection.getresponse().read())
    
    if 'error' in result.keys():
        print '\n', result, '\n'
        return jsonify({ 'error': "<strong>Error:</strong> Your login information was incorrect. Please try again."})
    
    else:
        session['username'] = result['username']
        session['sessionToken'] = result['sessionToken']
        session['uID'] = result['objectId']
        
        # stay logged in longer
        if remember == True:
        	session.permanent = True
        else:
        	session.permanent = False

        return jsonify({ 'username': username })


@application.route('/fblogin', methods=['POST'])
def fblogin():
    username = request.form.get('username', None)
    password = request.form.get('password', None)
    remember = request.form.get('remember', None)

    params = urllib.urlencode({"username":username,"password":password})
    connection.connect()
    connection.request('GET', '/1/login?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })
    
    result = json.loads(connection.getresponse().read())
    
    if 'error' in result.keys():
        print '\n', result, '\n'
        return jsonify({ 'error': "<strong>Error:</strong> Your login information was incorrect. Please try again."})
    
    else:
        session['username'] = result['username']
        session['sessionToken'] = result['sessionToken']
        session['uID'] = result['objectId']
        
        # stay logged in longer
        if remember == True:
            session.permanent = True
        else:
            session.permanent = False

        return jsonify({ 'username': username })


@application.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    session.pop('sessionToken', None)
    session.pop('uID', None)
    return redirect(url_for('index'))


@application.route('/register', methods=['POST'])
def register():
    username = request.form.get('username', None)
    email = request.form.get('email', None).lower()
    password = request.form.get('password', None)
    confirm = request.form.get('confirm', None)

    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email): 
        print 'email invalid'
        return jsonify({ 'email': "invalid" })

    if password != confirm: 
        print 'password no match'
        return jsonify({ 'password-invalid': "invalid" })

    else:
        connection.connect()
        connection.request('POST', '/1/users', json.dumps({
            "username": username,
            "password": password,
            "email": email
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
            print 'successful registration'
            session['username'] = username
        
            # stay logged in longer
            session.permanent = True

            return jsonify({ 'success': "Registration successful. You are now logged in." })


@application.route('/forgot', methods=['POST'])
def forgot():
    email = request.form.get('email', None).lower()

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