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
    
    params = urllib.urlencode({
        "order":"-createdAt",
        "limit": 12,
        "where":json.dumps({
           "cycleArticle": True,
           "cycle": 1
        })
    })
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })
    
    result = json.loads(connection.getresponse().read())

    articles = result['results']
    # print len(articles)
   
    return render_template("dashboard/cycle.html", articles=articles, cycle='Cycle #'+str(CURRCYCLE))

@dashboard.route('/current/<slug>')
def read_cycle(slug):
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "slug": slug
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
            return render_template("articles/article_feature.html", article=article, author=author)

    else:
        print 'error'
        return redirect(url_for('cycle'))


# --------------------------------------------------------------------------------
# Beauty
# --------------------------------------------------------------------------------
@dashboard.route('/beauty')
def beauty():
    connection.connect()
    params = urllib.urlencode({
        "order":"-createdAt",
        "limit": 12,
        "where":json.dumps({
           "$or": [
                {"category": "Fashion"},
                {"category": "Hair"},
                {"category": "Body"},
                {"category": "Beauty"}
            ]
        })
    })
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    articles = result['results']

    return render_template("dashboard/beauty.html", articles=articles, sub=None)

@dashboard.route('/beauty/fashion')
@dashboard.route('/beauty/hair')
@dashboard.route('/beauty/body')
def sub_beauty():
    path = request.path
    sub_category = path.split('/')[2]

    # print sub_category

    connection.connect()
    params = urllib.urlencode({
        "order":"-createdAt",
        "limit": 12,
        "where": json.dumps({
            "category": sub_category.capitalize()
        })
    })
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    articles = result['results']

    return render_template("dashboard/beauty.html", articles=articles, sub=sub_category)

@dashboard.route('/beauty/<slug>')
@dashboard.route('/beauty/fashion/<slug>')
@dashboard.route('/beauty/hair/<slug>')
@dashboard.route('/beauty/body/<slug>')
def read_beauty(slug):
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "slug": slug
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
            return render_template("articles/article_feature.html", article=article, author=author)

    else:
        print 'error'
        return redirect(url_for('beauty'))


# --------------------------------------------------------------------------------
# Career
# --------------------------------------------------------------------------------
@dashboard.route('/career')
def career():
    connection.connect()
    params = urllib.urlencode({
        "order":"-createdAt",
        "limit": 12,
        "where":json.dumps({
           "category": "Career"
        })
    })
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    articles = result['results']

    return render_template("dashboard/career.html", articles=articles, sub=None)

@dashboard.route('/career/<slug>')
def read_career(slug):
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "slug": slug
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
            return render_template("articles/article_feature.html", article=article, author=author)

    else:
        print 'error'
        return redirect(url_for('career'))


# --------------------------------------------------------------------------------
# Entertainment
# --------------------------------------------------------------------------------       
@dashboard.route('/entertainment')
def entertainment():
    connection.connect()
    params = urllib.urlencode({
        "order":"-createdAt",
        "limit": 12,
        "where":json.dumps({
           "$or": [
                {"category": "Entertainment"},
                {"category": "TV"},
                {"category": "Music"},
                {"category": "Theater"},
                {"category": "Film"}
            ]
        })
    })
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    articles = result['results']

    return render_template("dashboard/entertainment.html", articles=articles, sub=None)

@dashboard.route('/entertainment/tv')
@dashboard.route('/entertainment/music')
@dashboard.route('/entertainment/film')
@dashboard.route('/entertainment/theater')
def sub_entertainment():
    path = request.path
    sub_category = path.split('/')[2]

    connection.connect()
    params = urllib.urlencode({
        "order":"-createdAt",
        "limit": 12,
        "where":json.dumps({
            "category": sub_category.capitalize()
        })
    })
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    articles = result['results']

    return render_template("dashboard/entertainment.html", articles=articles, sub=sub_category)

@dashboard.route('/entertainment/<slug>')
@dashboard.route('/entertainment/tv/<slug>')
@dashboard.route('/entertainment/music/<slug>')
@dashboard.route('/entertainment/film/<slug>')
@dashboard.route('/entertainment/theater/<slug>')
def read_entertainment(slug):
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "slug": slug
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
            return render_template("articles/article_feature.html", article=article, author=author)

    else:
        print 'error'
        return redirect(url_for('entertainment'))


# --------------------------------------------------------------------------------
# Lifestyle
# -------------------------------------------------------------------------------- 
@dashboard.route('/lifestyle')
def lifestyle():
    connection.connect()
    params = urllib.urlencode({
        "order":"-createdAt",
        "limit": 12,
        "where":json.dumps({
           "$or": [
                {"category": "Lifestyle"},
                {"category": "Food"},
                {"category": "Drink"},
                {"category": "Travel"},
                {"category": "Spirit"},
                {"category": "Mind"},
                {"category": "Body"},
            ]
        })
    })
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    articles = result['results']

    return render_template("dashboard/lifestyle.html", articles=articles, sub=None)

@dashboard.route('/lifestyle/mind')
@dashboard.route('/lifestyle/body')
@dashboard.route('/lifestyle/spirit')
@dashboard.route('/lifestyle/fooddrink')
@dashboard.route('/lifestyle/travel')
def sub_lifestyle():
    path = request.path
    sub_category = path.split('/')[2]

    connection.connect()
    params = urllib.urlencode({
        "order":"-createdAt",
        "limit": 12,
        "where":json.dumps({
            "category": sub_category.capitalize()
        })
    })
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    articles = result['results']

    return render_template("dashboard/lifestyle.html", articles=articles, sub=sub_category)

@dashboard.route('/lifestyle/<slug>')
@dashboard.route('/lifestyle/mind/<slug>')
@dashboard.route('/lifestyle/body/<slug>')
@dashboard.route('/lifestyle/spirit/<slug>')
@dashboard.route('/lifestyle/fooddrink/<slug>')
@dashboard.route('/lifestyle/travel/<slug>')
def read_lifestyle(slug):
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "slug": slug
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
            return render_template("articles/article_feature.html", article=article, author=author)

    else:
        print 'error'
        return redirect(url_for('lifestyle'))


# --------------------------------------------------------------------------------
# Money
# -------------------------------------------------------------------------------- 
@dashboard.route('/money')
def money():
    connection.connect()
    params = urllib.urlencode({
        "order":"-createdAt",
        "limit": 12,
        "where":json.dumps({
            "category": "Money"
        })
    })
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    articles = result['results']

    return render_template("dashboard/money.html", articles=articles, sub=None)

@dashboard.route('/money/saving')
@dashboard.route('/money/spending')
@dashboard.route('/money/investing')
def sub_money():
    path = request.path
    sub_category = path.split('/')[2]

    connection.connect()
    params = urllib.urlencode({
        "order":"-createdAt",
        "limit": 12,
        "where":json.dumps({
            "category": sub_category.capitalize()
        })
    })
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    articles = result['results']

    return render_template("dashboard/money.html", articles=articles, sub=sub_category)

@dashboard.route('/money/<slug>')
@dashboard.route('/money/saving/<slug>')
@dashboard.route('/money/spending/<slug>')
@dashboard.route('/money/investing/<slug>')
def read_money(slug):
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "slug": slug
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
            return render_template("articles/article_feature.html", article=article, author=author)

    else:
        print 'error'
        return redirect(url_for('dashboard.money'))

# --------------------------------------------------------------------------------
# Wildcard
# -------------------------------------------------------------------------------- 
@dashboard.route('/wildcard')
def wildcard():
    connection.connect()
    params = urllib.urlencode({
        "order":"-createdAt",
        "limit": 12,
        "where":json.dumps({
            "category": "Wildcard"
        })
    })
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    articles = result['results']

    return render_template("dashboard/wildcard.html", articles=articles, sub=None)

@dashboard.route('/wildcard/giggles')
@dashboard.route('/wildcard/opinions')
def sub_wildcard():
    path = request.path
    sub_category = path.split('/')[2]

    connection.connect()
    params = urllib.urlencode({
        "order":"-createdAt",
        "limit": 12,
        "where":json.dumps({
            "category": sub_category.capitalize()
        })
    })
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    articles = result['results']

    return render_template("dashboard/wildcard.html", articles=articles, sub=sub_category)

@dashboard.route('/wildcard/<slug>')
@dashboard.route('/wildcard/giggles/<slug>')
@dashboard.route('/wildcard/opinions/<slug>')
def read_wildcard(slug):
    connection.connect()
    
    params = urllib.urlencode({"where":json.dumps({
       "slug": slug
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
            return render_template("articles/article_feature.html", article=article, author=author)

    else:
        print 'error'
        return redirect(url_for('dashboard.wildcard'))


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

