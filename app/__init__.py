from flask import Flask, render_template
# from flask.ext.mail import Message, Mail
from app.content.application import content as contentBP
from app.dashboard.application import dashboard as dashBP
from app.user.application import user as userBP


# create the application
app = Flask(__name__)
app.config.from_object('config')


# initialize email client - GMail
# mail = Mail(app)
# mail.init_app(app)


from app import application

# register the blueprints
app.register_blueprint(contentBP)
app.register_blueprint(dashBP)
app.register_blueprint(userBP)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404