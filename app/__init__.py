from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Message, Mail

# create the application
app = Flask(__name__)
app.config.from_object('config')

# initialize database
# db = SQLAlchemy(app)
# db.init_app(app)

# initialize email client - GMail
mail = Mail(app)
mail.init_app(app)

from app import application