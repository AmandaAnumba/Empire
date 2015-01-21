from flask import Flask, Blueprint, render_template, request, redirect, escape, jsonify, abort
from jinja2 import TemplateNotFound
# from ..emails import *

home = Blueprint('home', __name__)

# @home.route("/", defaults={'page': 'index'})
# @home.route('/<page>', methods=['GET', 'POST'])
# def show(page):
#     print "here"
#     print page

#     try:
#         if page == 'contact':
#             if request.method == 'GET':
#                 return render_template("home/contact.html")

#             elif request.method == 'POST':
#                 name = request.form.get('name', None)
#                 email = request.form.get('email', None)
#                 subject = request.form.get('subject', None)
#                 message = request.form.get('message', None)

#                 try:
#                     empireContact(name, email, subject, message)
#                     return jsonify({ 'success': "Your message has been sent. You will now be redirected to the front page." })

#                 except:
#                     return jsonify({ 'error': "Your email could not be sent. Please refresh the page and try again." })
#         else:
#             return render_template('home/%s.html' % page)
#     except TemplateNotFound:
#         abort(404)


@home.route("/")
def index():
    #display welcome page
    return render_template('home/index.html')

@home.route("/about")
def about():
    return render_template('home/about.html')

@home.route('/contact', methods=['GET', 'POST'])
def contact():
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
    
@home.route('/terms')
def terms():
    return render_template("home/terms.html")

@home.route('/privacy')
def privacy():
    return render_template("home/privacy.html")