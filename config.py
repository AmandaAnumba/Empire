#!/usr/bin/env python

# Statement for enabling the development environment
DEBUG = True

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

WTF_CSRF_ENABLED = True

secret = "pv8x2TBwDqznefu0P4vlcyWc"
# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = secret

# Secret key for signing cookies
SECRET_KEY = secret

# database configuration
SQLALCHEMY_DATABASE_URI = 'mysql://admin:923emp1r3@empire-db.cj8w2td4aocw.us-east-1.rds.amazonaws.com/empireDB?charset=utf8&use_unicode=0'
SQLALCHEMY_ECHO = True

# flask mail configurations
MAIL_SERVER = "mail.empire.life"
MAIL_PORT = 587
MAIL_USE_SSL = False
MAIL_USE_TLS = True
MAIL_USERNAME = 'help@empire.life'
MAIL_PASSWORD = '923emp1r3'





