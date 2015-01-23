from app import app
from flask import render_template, session, url_for, escape

# set after login
# session.permanent = True

application = app 

@application.route("/")
def index():
    # if session.get('username'):
    #     username = escape(session['username'])
    #     return render_template('home/dash_user.html', username=username)
    # else:
    return render_template('home/index.html')
