from flask.ext.mail import Message
from app import mail
from flask import render_template, url_for, current_app
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def send_email(subject, recipients, sender, html_body):
    msg = Message(subject, sender=sender, recipients=[recipients])
    msg.html = html_body
    mail.send(msg)

def empireContact(name, email, subject, message):
    send_email('Empire Contact form Submission', 'help@empire.life', email, render_template("emails/email_contact.html",name=name,email=email,subject=subject, msg=message))

