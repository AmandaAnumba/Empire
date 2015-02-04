from app import app
import os, random, sys, time, re, string, base64, hmac, urllib, json, httplib
from hashlib import sha1
from emails import *

from flask import flash, Flask, render_template, session, request, redirect, url_for, escape, jsonify

from werkzeug import secure_filename, check_password_hash, generate_password_hash
from werkzeug.exceptions import default_exceptions, HTTPException

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

@application.route("/")
def index():
    if session.get('username') and session.get('sessionToken') and session.get('uID'):
       	username = escape(session['username'])
       	return render_template('home/index.html', username=username, loggedin=True)
    else:
    	return render_template('home/index.html', username=None, loggedin=False)


@application.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = request.form['remember']

        # check to make sure user exists 
        params = urllib.urlencode({"username":username,"password":password})
        connection.connect()
        connection.request('GET', '/1/login?%s' % params, '', {
            "X-Parse-Application-Id": PARSEappID,
            "X-Parse-REST-API-Key": RESTapiKEY
        })
        
        result = json.loads(connection.getresponse().read())
        
        # print '\n', result, '\n'

        if 'error' in result.keys():
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

    elif request.method == 'GET':
        return redirect(url_for('index'))


@application.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    session.pop('sessionToken', None)
    session.pop('uID', None)
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
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

    elif request.method == 'GET':
        return redirect(url_for('index'))


@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    if request.method == 'POST':
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

    elif request.method == 'GET':
        return redirect(url_for('index'))

