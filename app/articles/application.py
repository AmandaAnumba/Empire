import os, random, sys, time, re, string, json, httplib, urllib
from flask import Flask, Blueprint, url_for, render_template, request, redirect, escape, jsonify, abort

articles = Blueprint('articles', __name__)

# Parse.com RESTful API
connection = httplib.HTTPSConnection('api.parse.com', 443)
ParseAppID = "ijqxeiardpj4GzolLOo2lhzegVopVBnn9bcHyIOs"
ParseRESTKey = "Rip5cgtxGNddTSe3yAoWdiIeJpMDALKJmUastpyf"


@articles.route('/r/<username>/<id>/<title>', methods=['GET'])
def read(username, id, title):
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "objectId": id
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": ParseAppID,
        "X-Parse-REST-API-Key": ParseRESTKey
    })
    
    result = json.loads(connection.getresponse().read())

    # print '\n', result, '\n'

    article = result['results'][0]

    if 'error' not in article.keys():
        uID = article['authorFull']['objectId']

        connection.request('GET', '/1/users/'+uID, '', {
            "X-Parse-Application-Id": ParseAppID,
            "X-Parse-REST-API-Key": ParseRESTKey
        })
        
        author = json.loads(connection.getresponse().read())

        # if article['doctype'] == 'regular':
        return render_template("articles/regular.html", article=article, author=author)

    #     if article['doctype'] == 'featured':
    #         return render_template("featured.html", article=article)

    # else:
    #     abort(400)


@articles.route('/rate', methods=['GET', 'POST'])
def rate():
    if request.method == 'GET':
        return redirect(url_for('cycle'))

    elif request.method == 'POST':
        articleID = request.form.get('id', None)
        action = request.form.get('action', None)

        print articleID, action

        connection.connect()
        connection.request('PUT', '/1/classes/Articles/'+articleID, json.dumps({
            action : {
                "__op": "Increment",
                "amount": 1
            }
        }), 
        {
            "X-Parse-Application-Id": "ijqxeiardpj4GzolLOo2lhzegVopVBnn9bcHyIOs",
            "X-Parse-REST-API-Key": "Rip5cgtxGNddTSe3yAoWdiIeJpMDALKJmUastpyf",
            "Content-Type": "application/json"
        })
        result = json.loads(connection.getresponse().read())

        print result

        if 'error' in result.keys():
            return jsonify({ 'error': "error" })

        else:
            return jsonify({ 'success': "success" })
            


@articles.route('/users/<username>')
def user(username):
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "username": username
    })})
    
    connection.request('GET', '/1/users?%s' % params, '', {
        "X-Parse-Application-Id": ParseAppID,
        "X-Parse-REST-API-Key": ParseRESTKey
    })
    
    result = json.loads(connection.getresponse().read())

    user = result['results'][0]

    return render_template("articles/profile.html", user=user)




