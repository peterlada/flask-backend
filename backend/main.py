from os import getenv as env

from flask import Flask
from flask.ext.sslify import SSLify
from flask.ext.mail import Mail
from raven.contrib.flask import Sentry


def create_app():
    app = Flask(__package__)
    app.config.from_pyfile('../config/' + env('BACKEND', 'dev') + '.py')

    from .models import db
    db.init_app(app)

    Mail(app)
    if app.config['SSL_REQUIRED']:
        print "boo"
        SSLify(app, permanent=True)
    if app.config['SENTRY_DSN']:
        Sentry(app)

    # register blueprints

    return app
