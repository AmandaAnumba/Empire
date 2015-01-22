import os, random, sys, time, re, string, json, httplib, urllib
from flask import Flask, Blueprint, url_for, render_template, request, redirect, escape, jsonify, abort

article = Blueprint('article', __name__)

# Parse.com RESTful API
connection = httplib.HTTPSConnection('api.parse.com', 443)

@article.route('/r/<username>/<id>/<title>', methods=['GET'])
def read(username, id, title):
    if username == 'static':
        print username
        return redirect(url_for('index'))
    
    else:
        connection.connect()
        
        params = urllib.urlencode({"where":json.dumps({
           "objectId": id
        })})
        
        connection.request('GET', '/1/classes/Articles?%s' % params, '', {
            "X-Parse-Application-Id": "ijqxeiardpj4GzolLOo2lhzegVopVBnn9bcHyIOs",
            "X-Parse-REST-API-Key": "Rip5cgtxGNddTSe3yAoWdiIeJpMDALKJmUastpyf"
        })
        
        result = json.loads(connection.getresponse().read())

        print '\n', result, '\n'

        article = result['results'][0]

        if 'error' not in article.keys():

            # if article['doctype'] == 'regular':
            return render_template("regular.html", article=article)

    #     if article['doctype'] == 'featured':
    #         return render_template("featured.html", article=article)

    # else:
    #     abort(400)


@article.route('/rate', methods=['GET', 'POST'])
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
            