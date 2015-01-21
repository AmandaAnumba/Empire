from app import app
import os, random, sys, time, re, string, json, httplib, urllib
# from emails import *

from flask import flash, Flask, Blueprint, render_template, session, request, redirect, url_for, escape, jsonify

from werkzeug import secure_filename, check_password_hash, generate_password_hash
from werkzeug.exceptions import default_exceptions, HTTPException

# set after login
# session.permanent = True

# dashboard = Blueprint('dashboard', __name__, template_folder='templates',)
application = app

# Parse.com RESTful API
connection = httplib.HTTPSConnection('api.parse.com', 443)


reload(sys)
sys.setdefaultencoding("utf-8")


# blue prints

# dashboard = Blueprint('dashboard', __name__, template_folder='templates')


@application.route('/current')
def cycle():
    # get all of the articles
    # articles = Articles.query.all()
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "status": "proofed"
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": "ijqxeiardpj4GzolLOo2lhzegVopVBnn9bcHyIOs",
        "X-Parse-REST-API-Key": "Rip5cgtxGNddTSe3yAoWdiIeJpMDALKJmUastpyf"
    })
    
    result = json.loads(connection.getresponse().read())

    articles = result['results']
    print len(articles)
   
    return render_template("cycle.html", articles=articles, category='Cycle #1')

# ##### categories ##### #
@application.route('/current-events')
def news():
    # get all of the articles
    # save to json with date and category
    # on load, check the time stamps, if more than
    # 30 mins, then check again
    connection.connect()

    params = urllib.urlencode({"where":json.dumps({
       "status": "proofed"
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": "ijqxeiardpj4GzolLOo2lhzegVopVBnn9bcHyIOs",
        "X-Parse-REST-API-Key": "Rip5cgtxGNddTSe3yAoWdiIeJpMDALKJmUastpyf"
    })

    result = json.loads(connection.getresponse().read())
    
    print result

    articles = result['results']
    a = []

    for i in articles:
        cat = [x.strip() for x in (i['category']).split(',')]

        if 'Politics' in cat:
            a.append(i)

    print a

    return render_template("cycle.html", articles=a, category='Current Events')

    # articles = Articles.query.all()
    # a = []

    # for i in articles:
    #     cat = [x.strip() for x in (i['category']).split(',')]

    #     if 'Politics' in cat:
    #         a.append(i)

    # return render_template("cycle.html", articles=a)

@application.route('/technology')
def tech():
    # get all of the articles
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "status": "proofed"
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": "ijqxeiardpj4GzolLOo2lhzegVopVBnn9bcHyIOs",
        "X-Parse-REST-API-Key": "Rip5cgtxGNddTSe3yAoWdiIeJpMDALKJmUastpyf"
    })

    result = json.loads(connection.getresponse().read())
    print result

    articles = result['results']
    a = []
    # articles = Articles.query.all()
    # a = []

    for i in articles:
        cat = [x.strip() for x in (i['category']).split(',')]

        if 'Technology' in cat:
            a.append(i)

    return render_template("cycle.html", articles=a, category='Technology')

@application.route('/money')
def money():
    # get all of the articles
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "status": "proofed"
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": "ijqxeiardpj4GzolLOo2lhzegVopVBnn9bcHyIOs",
        "X-Parse-REST-API-Key": "Rip5cgtxGNddTSe3yAoWdiIeJpMDALKJmUastpyf"
    })


    result = json.loads(connection.getresponse().read())
    print result

    articles = result['results']
    a = []

    # articles = Articles.query.all()
    # a = []

    for i in articles:
        cat = [x.strip() for x in (i['category']).split(',')]

        if 'Money' in cat:
            a.append(i)

    return render_template("cycle.html", articles=a, category='Money')

@application.route('/career')
def career():
    # get all of the articles
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "status": "proofed"
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": "ijqxeiardpj4GzolLOo2lhzegVopVBnn9bcHyIOs",
        "X-Parse-REST-API-Key": "Rip5cgtxGNddTSe3yAoWdiIeJpMDALKJmUastpyf"
    })


    result = json.loads(connection.getresponse().read())
    print result

    articles = result['results']
    a = []

    # articles = Articles.query.all()
    # a = []

    for i in articles:
        cat = [x.strip() for x in (i['category']).split(',')]

        if 'Career' in cat:
            a.append(i)

    return render_template("cycle.html", articles=a, category='Career')

@application.route('/mindbody')
def mindbody():
    # get all of the articles
    connection.connect()
    params = urllib.urlencode({"where":json.dumps({
       "status": "proofed"
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": "ijqxeiardpj4GzolLOo2lhzegVopVBnn9bcHyIOs",
        "X-Parse-REST-API-Key": "Rip5cgtxGNddTSe3yAoWdiIeJpMDALKJmUastpyf"
    })


    result = json.loads(connection.getresponse().read())
    print result

    articles = result['results']
    a = []

    # articles = Articles.query.all()
    # a = []

    for i in articles:
        cat = [x.strip() for x in (i['category']).split(',')]

        if 'Mind + Spirit' in cat or 'Relationships' in cat or 'Body + Beauty' in cat:
            a.append(i)

    return render_template("cycle.html", articles=a, category='Mind, Body, and Spirit')

@application.route('/culture')
def culture():
    # get all of the articles
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "status": "proofed"
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": "ijqxeiardpj4GzolLOo2lhzegVopVBnn9bcHyIOs",
        "X-Parse-REST-API-Key": "Rip5cgtxGNddTSe3yAoWdiIeJpMDALKJmUastpyf"
    })


    result = json.loads(connection.getresponse().read())
    print result

    articles = result['results']
    a = []

    # articles = Articles.query.all()
    # a = []

    for i in articles:
        cat = [x.strip() for x in (i['category']).split(',')]

        if 'TV + Music' in cat or 'Art + Fashion' in cat or 'Sports' in cat:
            a.append(i)

    return render_template("cycle.html", articles=a, category='Culture')

@application.route('/wildcard')
def wildcard():
    # get all of the articles
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "status": "proofed"
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": "ijqxeiardpj4GzolLOo2lhzegVopVBnn9bcHyIOs",
        "X-Parse-REST-API-Key": "Rip5cgtxGNddTSe3yAoWdiIeJpMDALKJmUastpyf"
    })


    result = json.loads(connection.getresponse().read())
    print result

    articles = result['results']
    a = []

    # articles = Articles.query.all()
    # a = []

    for i in articles:
        cat = [x.strip() for x in (i['category']).split(',')]

        if 'Wildcard' in cat:
            a.append(i)

    return render_template("cycle.html", articles=a, category='Wildcard')

# ##### categories ##### #

@application.route('/r/<username>/<id>/<title>')
def read(username, id, title):
    
    # article = Articles.query.filter_by(id=id).first()
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "objectId": id
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": "ijqxeiardpj4GzolLOo2lhzegVopVBnn9bcHyIOs",
        "X-Parse-REST-API-Key": "Rip5cgtxGNddTSe3yAoWdiIeJpMDALKJmUastpyf"
    })
    
    result = json.loads(connection.getresponse().read())

    print result

    article = result['results'][0]

    if 'error' not in article.keys():

        # if article['doctype'] == 'regular':
        return render_template("regular.html", article=article)

    #     if article['doctype'] == 'featured':
    #         return render_template("featured.html", article=article)

    # else:
    #     abort(400)


# @application.route('/article')
# def article():
#     # get all of the articles
#     articles = Articles.query.filter_by(status='ready').first()

#     return render_template("featured.html", article=articles)

# @application.route('/regular')
# def regular():
#     # get all of the articles
#     articles = Articles.query.filter_by(status='ready').first()

#     return render_template("regular.html", article=articles)

@application.route('/rate', methods=['GET', 'POST'])
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
            





