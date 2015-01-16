from application import db
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, Date, Float
from sqlalchemy.dialects import mysql
from werkzeug import check_password_hash, generate_password_hash


class User(db.Model):
    __tablename__ = 'users'
    id             = db.Column(db.Integer, primary_key=True)
    username       = db.Column(db.String(255), nullable=False, unique=True)
    email          = db.Column(db.String(255), nullable=False, unique=True)
    password       = db.Column(db.String(255), nullable=False)
    avatar         = db.Column(db.String(64), nullable=True)
    role           = db.Column(db.String(1), nullable=False)
    emailVerified  = db.Column(db.Integer, nullable=False)
    bio            = db.Column(mysql.TEXT, nullable=True)
    facebook       = db.Column(db.String(128), nullable=True)
    twitter        = db.Column(db.String(128), nullable=True)
    tumblr         = db.Column(db.String(128), nullable=True)
    website        = db.Column(db.String(128), nullable=True)
    fullname       = db.Column(db.String(255), nullable=True)
    

    # New instance instantiation procedure
    def __init__(self, username, email, password, role):
        self.username = username
        self.email    = email.lower()
        self.set_password(password)
        self.role     = role
        self.emailVerified = 0

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %r>' % (self.username)   


class Validation(db.Model):
    __tablename__ = 'code_generator'
    code    = db.Column(db.String(10), primary_key=True, nullable=False)
    userID  = db.Column(db.Integer, unique=True, nullable=False)
    timestamp  = db.Column(db.DateTime,  default=db.func.current_timestamp())

    def __init__(self, code, user):
        self.code   = code
        self.userID = user    

    def __repr__(self):
        return '<ID %r, Code %r>' % (self.userID, self.code) 


class Articles(db.Model):
    __tablename__ = 'articles'
    id              = db.Column(db.Integer, primary_key=True)
    title           = db.Column(db.String(255), nullable=True)
    author          = db.Column(db.String(255), nullable=True)
    description     = db.Column(mysql.MEDIUMTEXT, nullable=True)
    tags            = db.Column(mysql.MEDIUMTEXT, nullable=True)
    content         = db.Column(mysql.LONGTEXT, nullable=True)
    featureIMG      = db.Column(db.String(128), nullable=True)
    status          = db.Column(db.String(11), nullable=True)
    releaseDate     = db.Column(db.String(40), nullable=True)
    doctype         = db.Column(db.String(10), nullable=True)
    category        = db.Column(mysql.MEDIUMTEXT, nullable=True)
    headerIMG       = db.Column(db.String(128), nullable=True)
    coAuthor        = db.Column(db.String(255), nullable=True)
    photoCred       = db.Column(mysql.MEDIUMTEXT, nullable=True)
    date            = db.Column(mysql.DATE, nullable=True)
    comment         = db.Column(mysql.LONGTEXT, nullable=True)

    # New instance instantiation procedure
    def __init__(self, title, author, description, tags, content, featureIMG, status, releaseDate, doctype, category, headerIMG, coAuthor, photoCred):
        self.title = title
        self.author = author
        self.description = description
        self.tags = tags
        self.content = content
        self.featureIMG = featureIMG
        self.status     = status
        self.releaseDate = releaseDate
        self.doctype     = doctype
        self.category     = category
        self.headerIMG     = headerIMG
        self.coAuthor     = coAuthor
        self.photoCred     = photoCred

    def __repr__(self):
        return '<Article %r>' % (self.title)


