""" 
    blueprint for all user actions and page rendering

    Current Actions:
        - view and edit profile
        - subscribe to a topic
        - receive points
        - follow a user 

    Future Actions:
        - write an article
            * Op-Ed / opinion
            * Voices
            * Article 

"""

import string, json, httplib, urllib
from flask import Blueprint, url_for, render_template, session, request, redirect, escape, jsonify, abort



user = Blueprint('user', __name__)

# Parse.com RESTful API
connection = httplib.HTTPSConnection('api.parse.com', 443)
PARSEappID = "ijqxeiardpj4GzolLOo2lhzegVopVBnn9bcHyIOs"
RESTapiKEY = "Rip5cgtxGNddTSe3yAoWdiIeJpMDALKJmUastpyf"


@user.route('/profile', methods=['GET', 'POST'])
def editProfile():
    username = escape(session['username'])
    sessionToken = escape(session['sessionToken'])

    params = urllib.urlencode({"where":json.dumps({
        "username": username
    })})

    connection.connect()
    connection.request('GET', '/1/users/me', '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY,
        "X-Parse-Session-Token": sessionToken
    })

    result = json.loads(connection.getresponse().read())

    updates = {}

    user = result
 
    if request.method == 'GET':
        return render_template("user/edit_profile.html",user=user)

    elif request.method == 'POST':
        post = json.loads(request.data)

        fullname = post['data']['fullname']
        email = post['data']['email']
        bio = post['data']['bio']
        avatar = post['data']['avatar']
        website = post['data']['website']
        facebook = post['data']['facebook']
        tumblr = post['data']['tumblr']
        twitter = post['data']['twitter']
        pinterest = post['data']['pinterest']
        linkedin = post['data']['linkedin']
        instagram = post['data']['instagram']
        
        if fullname and (user['fullname'] != fullname):
            updates['fullname'] = fullname

        if avatar and (user['avatar'] != avatar):
            updates['avatar'] = avatar

        if bio and (user['bio'] != bio):
            updates['fullname'] = fullname

        if email and (user['email'] != email):
            updates['email'] = email

        if website and (user['website'] != website):
            updates['website'] = website

        if facebook and (user['facebook'] != facebook):
            updates['facebook'] = facebook

        if tumblr and (user['tumblr'] != tumblr):
            updates['tumblr'] = tumblr

        if twitter and (user['twitter'] != twitter):
            updates['twitter'] = twitter

        if linkedin and (user['linkedin'] != linkedin):
            updates['linkedin'] = linkedin

        if pinterest and (user['pinterest'] != pinterest):
            updates['pinterest'] = pinterest

        if instagram and (user['instagram'] != instagram):
            updates['instagram'] = instagram 

        connection.connect()
        connection.request('PUT', '/1/users/'+user['objectId'], json.dumps(updates),
        {
            "X-Parse-Application-Id": PARSEappID,
            "X-Parse-REST-API-Key": RESTapiKEY,
            "X-Parse-Session-Token": sessionToken,
            "Content-Type": "application/json"
        })

        result2 = json.loads(connection.getresponse().read())

        if 'error' in result2.keys():
            print 'error updating the user profile'
            return jsonify({ 'error': "Your profile information could not be saved. Please refresh the page and try again." })

        else:
            return jsonify({ 'success': "Your profile has been saved. Redirecting you to the home page..." })


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
    # update who the user follows
    # update the person being followed
    post = json.loads(request.data)

    followID = post['data']['followID']    
    userID = escape(session['uID'])
    sessionToken = escape(session['sessionToken'])
    
    try:
        connection.connect()
        connection.request('PUT', '/1/users/'+userID, json.dumps({
            "following": {
                "__op": "AddUnique",
                "objects": [
                    followID
                ]
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
            try:
                connection.request('PUT', '/1/users/'+followID, json.dumps({
                    "followers": {
                        "__op": "AddUnique",
                        "objects": [
                            userID
                        ]
                    }
                }), {
                    "X-Parse-Application-Id": PARSEappID,
                    "X-Parse-REST-API-Key": RESTapiKEY,
                    "X-Parse-Session-Token": sessionToken,
                    "Content-Type": "application/json"
                })
                
                result2 = json.loads(connection.getresponse().read())

                if 'error' in result.keys():
                    print result
                    return jsonify({ 'error': "There was an error in adding the points" })

                else:
                    return jsonify({ 'success': "success" })
            
            except:
                return jsonify({ 'fatalError': "An error occurred while trying to follow this user. Please refresh the page and try again. If the error persists, please contact support@empire.life ." })

    except:
        return jsonify({ 'fatalError': "An error occurred while trying to follow this user. Please refresh the page and try again. If the error persists, please contact support@empire.life ." })


# subscribe to a topic
# add the topic to their array of subscriptions
# when they come to Empire, their dashboard will be
# loaded with the newest articles from those sections
@user.route('/subscribe', methods=['POST'])
def subscribe():
    post = json.loads(request.data)

    topic = post['data']['topic']
    userID = escape(session['uID'])
    sessionToken = escape(session['sessionToken'])
    
    connection.connect()
    connection.request('PUT', '/1/users/'+userID, json.dumps({
        "subscriptions": {
            "__op": "AddUnique",
            "objects": [
                topic
            ]
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


