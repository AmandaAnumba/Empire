from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask.ext.uploads import UploadSet, IMAGES
from wtforms import TextField, DateField, RadioField, SelectField, BooleanField, TextAreaField, StringField, PasswordField, HiddenField, validators
from wtforms.validators import Email, InputRequired, ValidationError
from models import User


images = UploadSet('images', IMAGES)


class LoginForm(Form):
    username = TextField('Username')  
    password = PasswordField('Password')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)


class RegisterForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=30)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.Length(min=6, max=35, message='Error: Password must be at least 6 characters long'),
        validators.EqualTo('confirm', message='Error: Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(username = self.username.data).first()
        email = User.query.filter_by(email = self.email.data.lower()).first()
        
        if user:
            self.errors.append("This username is already taken")
            print 'error'
            return False
        if email:
            self.errors.append("This email address is already taken")
            print 'email error'
            return False
        else:
            return True


class Reset(Form):
    email = TextField()


class RegValidation(Form):
    code = TextField()
    password = PasswordField()
    confirm = PasswordField()
    reset = HiddenField()
    actionType = HiddenField()


class WriteForm(Form):
    title = TextField('Title') 
    author = TextField('Author') 
    tagline = TextAreaField('Tag line') 
    release = DateField(format='%m-%d-%Y')
    taginput = StringField()
    tags = HiddenField()
    text = HiddenField()
    date = HiddenField()
    doctype = RadioField('Article Type', choices=[('feature', 'feature'), ('regular', 'regular'), ('sponsored', 'sponsored')])
    featureIMG = FileField('image', validators=[
        FileRequired(),
        FileAllowed(images, 'Images only!')
    ])


class Profile(Form):
    first = TextField('First Name')
    last = TextField('Last Name')
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    bio = TextAreaField()
    avatar = FileField('image', validators=[
        FileRequired(),
        FileAllowed(images, 'Images only!')
    ])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Error: Passwords must match')
    ])
    confirm = PasswordField('Confirm Password', [
        validators.Required()
    ])
    website = TextField()
    facebook = TextField()
    tumblr = TextField()
    twitter = TextField()


class Contact(Form):
    name = TextField()
    email = TextField()
    subject = SelectField('Subject', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    message = TextAreaField()
   



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