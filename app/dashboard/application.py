"""
    This is the blueprint for monitoring and regulating the users dashboard
    
    Current Actions:
        - view dash
        - add category subscriptions

    Future Actions:
"""

import re, string, json, httplib, urllib
from flask import session, Blueprint, render_template, request, redirect, escape, jsonify



dashboard = Blueprint('dashboard', __name__)

# Globals
# --------------
CURRCYCLE = 1

# Parse.com RESTful API
connection = httplib.HTTPSConnection('api.parse.com', 443)
PARSEappID = "ijqxeiardpj4GzolLOo2lhzegVopVBnn9bcHyIOs"
RESTapiKEY = "Rip5cgtxGNddTSe3yAoWdiIeJpMDALKJmUastpyf"


@dashboard.route('/myhome')
def viewdash():
    try:
        username = escape(session['username'])
        return render_template('user/dash_user.html',username=username)

    except KeyError: 
        return redirect(url_for('home'))
