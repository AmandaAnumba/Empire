from flask import Flask, render_template
from flask.ext.mail import Message, Mail
from app.home.application import home as homeBP
from app.dashboard.application import dashboard as dashBP


# create the application
app = Flask(__name__)
app.config.from_object('config')


# initialize email client - GMail
mail = Mail(app)
mail.init_app(app)


# register the blueprints=
app.register_blueprint(homeBP)
app.register_blueprint(dashBP)


from app import application

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404