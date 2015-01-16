from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask.ext.uploads import UploadSet, IMAGES
from wtforms import TextField, DateField, RadioField, SelectField, BooleanField, TextAreaField, StringField, PasswordField, HiddenField, validators
from wtforms.validators import Email, InputRequired, ValidationError
from models import User


images = UploadSet('images', IMAGES)


class LoginForm(Form):
    username = TextField()  
    password = PasswordField()

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
   

