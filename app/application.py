from app import app
import os, random, sys, time, re, string, json, httplib, urllib
# from emails import *

from flask import flash, Flask,  safe_join, send_from_directory, Blueprint, render_template, session, request, redirect, url_for, escape, jsonify

from werkzeug import secure_filename, check_password_hash, generate_password_hash
from werkzeug.exceptions import default_exceptions, HTTPException

# set after login
# session.permanent = True

application = app

@application.route("/")
def index():
    return render_template('home/index.html')

@application.route('/<any(css, js, img, fonts, sound):folder>/<path:filename>')
def toplevel_static(folder, filename):
    filename = safe_join(folder, filename)
    cache_timeout = app.get_send_file_max_age(filename)
    return send_from_directory(app.static_folder, filename, cache_timeout=cache_timeout)

@application.route('/<path:filename>')
def public(filename):
    return render_template(filename)