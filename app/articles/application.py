import os, random, sys, time, re, string, json, httplib, urllib
from flask import Flask, Blueprint, url_for, render_template, request, redirect, escape, jsonify, abort

articles = Blueprint('articles', __name__)

# Parse.com RESTful API
connection = httplib.HTTPSConnection('api.parse.com', 443)
ParseAppID = "ijqxeiardpj4GzolLOo2lhzegVopVBnn9bcHyIOs"
ParseRESTKey = "Rip5cgtxGNddTSe3yAoWdiIeJpMDALKJmUastpyf"


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
   
            
# search for an article
@articles.route('/search', methods=['POST'])
def search():
    searchTerm = request.form.get('searchTerm', None)
    search = searchTerm.split()

    connection.connect()
    params = urllib.urlencode({"where":json.dumps({
       "$or": [
            {"category": "Entertainment"},
            {"category": "TV"},
            {"category": "Music"},
            {"category": "Theater"},
            {"category": "Film"}
        ]
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    articles = result['results']

    return render_template("dashboard/entertainment.html", articles=articles, sub=None)

    if 'error' in result.keys():
        return jsonify({ 'error': "error" })

    else:
        return jsonify({ 'success': "success" })

