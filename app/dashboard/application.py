import os, random, sys, time, re, string, json, httplib, urllib
from werkzeug.routing import AnyConverter
from flask import Flask, Blueprint, render_template, request, redirect, escape, jsonify, abort
from jinja2 import TemplateNotFound

dashboard = Blueprint('dashboard', __name__)

# Globals
# --------------
CURRCYCLE = 1

# Parse.com RESTful API
connection = httplib.HTTPSConnection('api.parse.com', 443)
PARSEappID = "ijqxeiardpj4GzolLOo2lhzegVopVBnn9bcHyIOs"
RESTapiKEY = "Rip5cgtxGNddTSe3yAoWdiIeJpMDALKJmUastpyf" 


# --------------------------------------------------------------------------------
# Cycle
# --------------------------------------------------------------------------------
@dashboard.route('/current')
def cycle():
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
   
    return render_template("dashboard/cycle.html", articles=articles, cycle='Cycle #'+str(CURRCYCLE))

@dashboard.route('/current/<title>/<id>')
def read_cycle(title,id):
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "objectId": id
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    article = result['results'][0]

    if 'error' not in article.keys():
        uID = article['authorFull']['objectId']

        connection.connect()
        connection.request('GET', '/1/users/'+uID, '', {
            "X-Parse-Application-Id": PARSEappID,
            "X-Parse-REST-API-Key": RESTapiKEY
        })
        
        author = json.loads(connection.getresponse().read())

        if article['doctype'] == 'regular':
            return render_template("articles/article_regular.html", article=article, author=author)

        elif article['doctype'] == 'feature':
            return render_template("articles/featured.html", article=article, author=author)

    else:
        print 'error'
        return render_template("articles/featured.html", article=article, author=author)


# --------------------------------------------------------------------------------
# Beauty
# --------------------------------------------------------------------------------
@dashboard.route('/beauty')
def beauty():
    connection.connect()
    params = urllib.urlencode({"where":json.dumps({
       "status": "published",
       "$or": [
            {"category1": "Fashion"},
            {"category1": "Hair"},
            {"category1": "Body"},
            {"category1": "Beauty"}
        ]
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    articles = result['results']

    return render_template("dashboard/beauty.html", articles=articles, sub=None)

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

    return render_template("dashboard/beauty.html", articles=articles, sub=sub_category)

@dashboard.route('/beauty/<title>/<id>')
@dashboard.route('/beauty/fashion/<title>/<id>')
@dashboard.route('/beauty/hair/<title>/<id>')
@dashboard.route('/beauty/body/<title>/<id>')
def read_beauty(title,id):
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "objectId": id
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    article = result['results'][0]

    if 'error' not in article.keys():
        uID = article['authorFull']['objectId']

        connection.connect()
        connection.request('GET', '/1/users/'+uID, '', {
            "X-Parse-Application-Id": PARSEappID,
            "X-Parse-REST-API-Key": RESTapiKEY
        })
        
        author = json.loads(connection.getresponse().read())

        if article['doctype'] == 'regular':
            return render_template("articles/article_regular.html", article=article, author=author)

        elif article['doctype'] == 'feature':
            return render_template("articles/featured.html", article=article, author=author)

    else:
        print 'error'
        return render_template("articles/featured.html", article=article, author=author)


# --------------------------------------------------------------------------------
# Career
# --------------------------------------------------------------------------------
@dashboard.route('/career')
def career():
    connection.connect()
    params = urllib.urlencode({"where":json.dumps({
       "status": "published",
       "category1": "Career"
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    articles = result['results']

    return render_template("dashboard/career.html", articles=articles, sub=None)

@dashboard.route('/career/<title>/<id>')
def read_career(title,id):
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "objectId": id
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    article = result['results'][0]

    if 'error' not in article.keys():
        uID = article['authorFull']['objectId']

        connection.connect()
        connection.request('GET', '/1/users/'+uID, '', {
            "X-Parse-Application-Id": PARSEappID,
            "X-Parse-REST-API-Key": RESTapiKEY
        })
        
        author = json.loads(connection.getresponse().read())

        if article['doctype'] == 'regular':
            return render_template("articles/article_regular.html", article=article, author=author)

        elif article['doctype'] == 'feature':
            return render_template("articles/featured.html", article=article, author=author)

    else:
        print 'error'
        return render_template("articles/featured.html", article=article, author=author)


# --------------------------------------------------------------------------------
# Entertainment
# --------------------------------------------------------------------------------       
@dashboard.route('/entertainment')
def entertainment():
    connection.connect()
    params = urllib.urlencode({"where":json.dumps({
       "status": "published",
       "$or": [
            {"category1": "Entertainment"},
            {"category1": "TV"},
            {"category1": "Music"},
            {"category1": "Theater"},
            {"category1": "Film"}
        ]
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    articles = result['results']

    return render_template("dashboard/entertainment.html", articles=articles, sub=None)

@dashboard.route('/entertainment/<sub_category>')
def sub_entertainment(sub_category):
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

    return render_template("dashboard/entertainment.html", articles=articles, sub=sub_category)

@dashboard.route('/entertainment/<title>/<id>')
@dashboard.route('/entertainment/tv/<title>/<id>')
@dashboard.route('/entertainment/music/<title>/<id>')
@dashboard.route('/entertainment/film/<title>/<id>')
@dashboard.route('/entertainment/theater/<title>/<id>')
def read_entertainment(title,id):
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "objectId": id
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    article = result['results'][0]

    if 'error' not in article.keys():
        uID = article['authorFull']['objectId']

        connection.connect()
        connection.request('GET', '/1/users/'+uID, '', {
            "X-Parse-Application-Id": PARSEappID,
            "X-Parse-REST-API-Key": RESTapiKEY
        })
        
        author = json.loads(connection.getresponse().read())

        if article['doctype'] == 'regular':
            return render_template("articles/article_regular.html", article=article, author=author)

        elif article['doctype'] == 'feature':
            return render_template("articles/featured.html", article=article, author=author)

    else:
        print 'error'
        return render_template("articles/featured.html", article=article, author=author)


# --------------------------------------------------------------------------------
# Lifestyle
# -------------------------------------------------------------------------------- 
@dashboard.route('/lifestyle')
def lifestyle():
    connection.connect()
    params = urllib.urlencode({"where":json.dumps({
       "status": "published",
       "$or": [
            {"category1": "Lifestyle"},
            {"category1": "Food"},
            {"category1": "Drink"},
            {"category1": "Travel"},
            {"category1": "Spirit"},
            {"category1": "Mind"},
            {"category1": "Body"},
        ]
       
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    articles = result['results']

    return render_template("dashboard/lifestyle.html", articles=articles, sub=None)

@dashboard.route('/lifestyle/<sub_category>')
def sub_lifestyle(sub_category):
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

    return render_template("dashboard/lifestyle.html", articles=articles, sub=sub_category)

@dashboard.route('/lifestyle/<title>/<id>')
@dashboard.route('/lifestyle/tv/<title>/<id>')
@dashboard.route('/lifestyle/music/<title>/<id>')
@dashboard.route('/lifestyle/film/<title>/<id>')
@dashboard.route('/lifestyle/theater/<title>/<id>')
def read_lifestyle(title,id):
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "objectId": id
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    article = result['results'][0]

    if 'error' not in article.keys():
        uID = article['authorFull']['objectId']

        connection.connect()
        connection.request('GET', '/1/users/'+uID, '', {
            "X-Parse-Application-Id": PARSEappID,
            "X-Parse-REST-API-Key": RESTapiKEY
        })
        
        author = json.loads(connection.getresponse().read())

        if article['doctype'] == 'regular':
            return render_template("articles/article_regular.html", article=article, author=author)

        elif article['doctype'] == 'feature':
            return render_template("articles/featured.html", article=article, author=author)

    else:
        print 'error'
        return render_template("articles/featured.html", article=article, author=author)


# --------------------------------------------------------------------------------
# Money
# -------------------------------------------------------------------------------- 
@dashboard.route('/money')
def money():
    connection.connect()
    params = urllib.urlencode({"where":json.dumps({
       "status": "published",
       "category1": "Money"
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    articles = result['results']

    return render_template("dashboard/money.html", articles=articles, sub=None)

@dashboard.route('/money/<sub_category>')
def sub_money(sub_category):
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

    return render_template("dashboard/money.html", articles=articles, sub=sub_category)

@dashboard.route('/money/<title>/<id>')
@dashboard.route('/money/saving/<title>/<id>')
@dashboard.route('/money/spending/<title>/<id>')
@dashboard.route('/money/investing/<title>/<id>')
def read_money(title,id):
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "objectId": id
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    article = result['results'][0]

    if 'error' not in article.keys():
        uID = article['authorFull']['objectId']

        connection.connect()
        connection.request('GET', '/1/users/'+uID, '', {
            "X-Parse-Application-Id": PARSEappID,
            "X-Parse-REST-API-Key": RESTapiKEY
        })
        
        author = json.loads(connection.getresponse().read())

        if article['doctype'] == 'regular':
            return render_template("articles/article_regular.html", article=article, author=author)

        elif article['doctype'] == 'feature':
            return render_template("articles/featured.html", article=article, author=author)

    else:
        print 'error'
        return render_template("articles/featured.html", article=article, author=author)


# --------------------------------------------------------------------------------
# Wildcard
# -------------------------------------------------------------------------------- 
@dashboard.route('/wildcard')
def wildcard():
    connection.connect()
    params = urllib.urlencode({"where":json.dumps({
       "status": "published",
       "category1": "Wildcard"
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    articles = result['results']

    return render_template("dashboard/wildcard.html", articles=articles, sub=None)

@dashboard.route('/wildcard/<sub_category>')
def sub_wildcard(sub_category):
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

    return render_template("dashboard/wildcard.html", articles=articles, sub=sub_category)

@dashboard.route('/wildcard/<title>/<id>')
@dashboard.route('/wildcard/giggles/<title>/<id>')
@dashboard.route('/wildcard/opinions/<title>/<id>')
def read_wildcard(title,id):
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "objectId": id
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    article = result['results'][0]

    if 'error' not in article.keys():
        uID = article['authorFull']['objectId']

        connection.connect()
        connection.request('GET', '/1/users/'+uID, '', {
            "X-Parse-Application-Id": PARSEappID,
            "X-Parse-REST-API-Key": RESTapiKEY
        })
        
        author = json.loads(connection.getresponse().read())

        if article['doctype'] == 'regular':
            return render_template("articles/article_regular.html", article=article, author=author)

        elif article['doctype'] == 'feature':
            return render_template("articles/featured.html", article=article, author=author)

    else:
        print 'error'
        return render_template("articles/featured.html", article=article, author=author)


# --------------------------------------------------------------------------------
# Legacy
# -------------------------------------------------------------------------------- 
@dashboard.route('/news')
def news():
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

@dashboard.route('/tech')
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

        if 'Money' in cat:
            a.append(i)

    return render_template("dashboard/cycle.html", articles=a, category='Money')

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