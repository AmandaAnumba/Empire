import os, random, sys, time, re, string, json, httplib, urllib
from flask import Flask, Blueprint, render_template, request, redirect, escape, jsonify, abort
from jinja2 import TemplateNotFound

dashboard = Blueprint('dashboard', __name__)

# Parse.com RESTful API
connection = httplib.HTTPSConnection('api.parse.com', 443)
PARSEappID = "ijqxeiardpj4GzolLOo2lhzegVopVBnn9bcHyIOs"
RESTapiKEY = "Rip5cgtxGNddTSe3yAoWdiIeJpMDALKJmUastpyf" 


@dashboard.route('/current')
def cycle():
    # get all of the articles
    # articles = Articles.query.all()
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "status": "published",
       "cycleArticle": True
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": "ijqxeiardpj4GzolLOo2lhzegVopVBnn9bcHyIOs",
        "X-Parse-REST-API-Key": "Rip5cgtxGNddTSe3yAoWdiIeJpMDALKJmUastpyf"
    })
    
    result = json.loads(connection.getresponse().read())

    articles = result['results']
    print len(articles)
   
    return render_template("dashboard/cycle.html", articles=articles, category='Cycle #1')


@dashboard.route('/beauty')
def beauty():
    connection.connect()
    params = urllib.urlencode({"where":json.dumps({
       "status": "published",
       "category1": "Beauty"
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    articles = result['results']

    return render_template("dashboard/beauty.html", articles=articles)


@dashboard.route('/beauty/<sub_category>')
def sub_beauty(sub_category):
    connection.connect()
    params = urllib.urlencode({"where":json.dumps({
       "status": "published",
       "category1": sub_category.capitalize()
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    articles = result['results']

    return render_template("dashboard/beauty.html", articles=articles)


@dashboard.route('/career')
def career():
    # get all of the articles
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "status": "published"
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
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

    return render_template("dashboard/cycle.html", articles=a, category='Career')


@dashboard.route('/money')
def money():
    # get all of the articles
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "status": "published"
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
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

    return render_template("dashboard/cycle.html", articles=a, category='Money')


@dashboard.route('/wildcard')
def wildcard():
    # get all of the articles
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "status": "published"
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
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

    return render_template("dashboard/cycle.html", articles=a, category='Wildcard')


@dashboard.route('/current-events')
def news():
    # get all of the articles
    # save to json with date and category
    # on load, check the time stamps, if more than
    # 30 mins, then check again
    connection.connect()

    params = urllib.urlencode({"where":json.dumps({
       "status": "published"
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
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

    return render_template("dashboard/cycle.html", articles=a, category='Current Events')

    # articles = Articles.query.all()
    # a = []

    # for i in articles:
    #     cat = [x.strip() for x in (i['category']).split(',')]

    #     if 'Politics' in cat:
    #         a.append(i)

    # return render_template("dashboard/cycle.html", articles=a)

@dashboard.route('/technology')
def tech():
    # get all of the articles
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "status": "published"
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
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

    return render_template("dashboard/cycle.html", articles=a, category='Technology')



@dashboard.route('/mindbody')
def mindbody():
    # get all of the articles
    connection.connect()
    params = urllib.urlencode({"where":json.dumps({
       "status": "published"
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
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

    return render_template("dashboard/cycle.html", articles=a, category='Mind, Body, and Spirit')

@dashboard.route('/culture')
def culture():
    # get all of the articles
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "status": "published"
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
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

    return render_template("dashboard/cycle.html", articles=a, category='Culture')

