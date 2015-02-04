@articles.route('/r/<category>/<sub>/<title>/<id>')
def read(category,sub,title,id):
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

    # print article

    if 'error' not in article.keys():
        uID = article['authorFull']['objectId']

        connection.connect()
        connection.request('GET', '/1/users/'+uID, '', {
            "X-Parse-Application-Id": ParseAppID,
            "X-Parse-REST-API-Key": ParseRESTKey
        })
        
        author = json.loads(connection.getresponse().read())

        if article['doctype'] == 'regular':
            return render_template("articles/article_regular.html", article=article, author=author)

        elif article['doctype'] == 'feature':
            return render_template("articles/featured.html", article=article, author=author)

    else:
        print 'error'
        return render_template("articles/featured.html", article=article, author=author)

@home.route("/", defaults={'page': 'index'})
@home.route('/<page>', methods=['GET', 'POST'])
def show(page):
    print "here"
    print page

    try:
        if page == 'contact':
            if request.method == 'GET':
                return render_template("home/contact.html")

            elif request.method == 'POST':
                name = request.form.get('name', None)
                email = request.form.get('email', None)
                subject = request.form.get('subject', None)
                message = request.form.get('message', None)

                try:
                    empireContact(name, email, subject, message)
                    return jsonify({ 'success': "Your message has been sent. You will now be redirected to the front page." })

                except:
                    return jsonify({ 'error': "Your email could not be sent. Please refresh the page and try again." })
        else:
            return render_template('home/%s.html' % page)
    except TemplateNotFound:
        abort(404)