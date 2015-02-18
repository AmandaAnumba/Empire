import re, string, json, httplib, urllib
from flask import Blueprint, render_template, request, redirect, escape, jsonify

content = Blueprint('content', __name__)

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
@content.route('/current')
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
   
    return render_template("articles/cycle.html", articles=articles, cycle='Cycle #'+str(CURRCYCLE))

@content.route('/current/<slug>')
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
@content.route('/beauty')
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

    return render_template("articles/beauty.html", articles=articles, sub=None)

@content.route('/beauty/fashion')
@content.route('/beauty/hair')
@content.route('/beauty/body')
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

    return render_template("articles/beauty.html", articles=articles, sub=sub_category)

@content.route('/beauty/<slug>')
@content.route('/beauty/fashion/<slug>')
@content.route('/beauty/hair/<slug>')
@content.route('/beauty/body/<slug>')
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
@content.route('/career')
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

    return render_template("articles/career.html", articles=articles, sub=None)

@content.route('/career/<slug>')
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
@content.route('/entertainment')
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

    return render_template("articles/entertainment.html", articles=articles, sub=None)

@content.route('/entertainment/tv')
@content.route('/entertainment/music')
@content.route('/entertainment/film')
@content.route('/entertainment/theater')
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

    return render_template("articles/entertainment.html", articles=articles, sub=sub_category)

@content.route('/entertainment/<slug>')
@content.route('/entertainment/tv/<slug>')
@content.route('/entertainment/music/<slug>')
@content.route('/entertainment/film/<slug>')
@content.route('/entertainment/theater/<slug>')
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
@content.route('/lifestyle')
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

    return render_template("articles/lifestyle.html", articles=articles, sub=None)

@content.route('/lifestyle/mind')
@content.route('/lifestyle/body')
@content.route('/lifestyle/spirit')
@content.route('/lifestyle/fooddrink')
@content.route('/lifestyle/travel')
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

    return render_template("articles/lifestyle.html", articles=articles, sub=sub_category)

@content.route('/lifestyle/<slug>')
@content.route('/lifestyle/mind/<slug>')
@content.route('/lifestyle/body/<slug>')
@content.route('/lifestyle/spirit/<slug>')
@content.route('/lifestyle/fooddrink/<slug>')
@content.route('/lifestyle/travel/<slug>')
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
@content.route('/money')
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

    return render_template("articles/money.html", articles=articles, sub=None)

@content.route('/money/saving')
@content.route('/money/spending')
@content.route('/money/investing')
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

    return render_template("articles/money.html", articles=articles, sub=sub_category)

@content.route('/money/<slug>')
@content.route('/money/saving/<slug>')
@content.route('/money/spending/<slug>')
@content.route('/money/investing/<slug>')
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
        return redirect(url_for('articles.money'))

# --------------------------------------------------------------------------------
# Wildcard
# -------------------------------------------------------------------------------- 
@content.route('/wildcard')
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

    return render_template("articles/wildcard.html", articles=articles, sub=None)

@content.route('/wildcard/giggles')
@content.route('/wildcard/opinions')
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

    return render_template("articles/wildcard.html", articles=articles, sub=sub_category)

@content.route('/wildcard/<slug>')
@content.route('/wildcard/giggles/<slug>')
@content.route('/wildcard/opinions/<slug>')
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
        return redirect(url_for('articles.wildcard'))


# =========================================================================
# =========================================================================
# ------------- Functions ------------- 
# =========================================================================
# =========================================================================
@content.route('/rate', methods=['GET', 'POST'])
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
            return jsonify({ "error": "error" })

        else:
            return jsonify({ "success": "success" })
   

# search for an article
@content.route('/search', methods=['POST'])
def search():
    post = json.loads(request.data)
    stoplist = ['a', 'an', 'as', 'are', 'aren\'t', 'at',\
                'be', 'because', 'but', 'by', 'is', 'it',\
                'isn\'t', 'its', 'it\'s', 'of', 'or', 'the',\
                'that', 'to', 'what', 'when', 'where', 'with', \
                'had', 'has', 'hasn\'t', 'have', 'for', 'do', 'does']

    searchTerm = post['searchTerm']
    y = searchTerm.lower().split(' ')
    search = []    

    for i in y and i not in stoplist:
        search.append({"search": i})
    
    connection.connect()
    params = urllib.urlencode({"where":json.dumps({
        "$or": search
    })})
    
    connection.request('GET', '/1/classes/Articles?%s' % params, '', {
        "X-Parse-Application-Id": PARSEappID,
        "X-Parse-REST-API-Key": RESTapiKEY
    })

    result = json.loads(connection.getresponse().read())

    if 'error' in result.keys():
        print result
        return jsonify({ 'error': "error" })

    else:
        items = result['results']
        
        if len(items) > 0:
            return jsonify({ 'data': items })
        else:
            return jsonify({ 'nodata': 'No articles matching your search query could be found. Try rephrasing your search.' })


