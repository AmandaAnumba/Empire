from app import app
import os, random, sys, time, re, string, base64, hmac, urllib, json, httplib
from hashlib import sha1
from emails import *

from flask import flash, Flask, render_template, session, request, redirect, url_for, escape, jsonify

from werkzeug import secure_filename, check_password_hash, generate_password_hash
from werkzeug.exceptions import default_exceptions, HTTPException

# set after login
# session.permanent = True

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
    if session.get('username'):
       	username = escape(session['username'])
       	return render_template('home/index.html', username=username)
    else:
    	return render_template('home/index.html')


@app.route('/login', methods=['GET', 'POST'])
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

            return jsonify({ 'success': "success" })

    elif request.method == 'GET':
        return redirect(url_for('index'))
