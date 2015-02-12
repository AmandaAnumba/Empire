import string, json, httplib, urllib
from flask import Blueprint, url_for, render_template, request, redirect, escape, jsonify, abort

""" 
    blueprint for all user actions and page rendering

"""

user = Blueprint('user', __name__)

# Parse.com RESTful API
connection = httplib.HTTPSConnection('api.parse.com', 443)
PARSEappID = "ijqxeiardpj4GzolLOo2lhzegVopVBnn9bcHyIOs"
RESTapiKEY = "Rip5cgtxGNddTSe3yAoWdiIeJpMDALKJmUastpyf"


@user.route('/_<username>')
def viewProfile(username):
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "username": username
    })})
    
    connection.request('GET', '/1/users?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })
    
    result = json.loads(connection.getresponse().read())

    user = result['results'][0]

    return render_template("user/profile.html", user=user)


# points system
@user.route('/points', methods=['POST'])
def points():
    amount = request.form.get('amount', None)
    userID = escape(session['uID'])
    sessionToken = escape(session['sessionToken'])
    
    connection.connect()
    connection.request('PUT', '/1/users/'+user['objectId'], json.dumps({
        "points": {
            "__op": "Increment",
            "amount": amount
        }
    }), {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY,
        "X-Parse-Session-Token": sessionToken,
        "Content-Type": "application/json"
    })

    result = json.loads(connection.getresponse().read())

    if 'error' in result.keys():
        print result
        return jsonify({ 'error': "There was an error in adding the points" })

    else:
        return jsonify({ 'success': "success" })


# follow a user
@user.route('/follow', methods=['POST'])
def follow():
    # update the follower
    # update the following
    
    followID = request.form.get('followID', None)
    userID = escape(session['uID'])
    sessionToken = escape(session['sessionToken'])
    
    connection.connect()
    connection.request('PUT', '/1/users/'+user['objectId'], json.dumps({
        
    }), {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY,
        "X-Parse-Session-Token": sessionToken,
        "Content-Type": "application/json"
    })

    result = json.loads(connection.getresponse().read())

    if 'error' in result.keys():
        print result
        return jsonify({ 'error': "There was an error in adding the points" })

    else:
        return jsonify({ 'success': "success" })


# subscribe to a topic
# add the topic to their array of subscriptions
# when they come to Empire, their dashboard will be
# loaded with the newest articles from those sections
@user.route('/subscribe', methods=['POST'])
def subscribe():
    amount = request.form.get('amount', None)
    userID = escape(session['uID'])
    sessionToken = escape(session['sessionToken'])
    
    connection.connect()
    connection.request('PUT', '/1/users/'+user['objectId'], json.dumps({
        "points": {
            "__op": "Increment",
            "amount": amount
        }
    }), {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY,
        "X-Parse-Session-Token": sessionToken,
        "Content-Type": "application/json"
    })

    result = json.loads(connection.getresponse().read())

    if 'error' in result.keys():
        print result
        return jsonify({ 'error': "There was an error in adding the points" })

    else:
        return jsonify({ 'success': "success" })
