from os import getenv as env

from flask import Flask
from flask.ext.sslify import SSLify
from flask.ext.mail import Mail


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config/' + env('BACKEND', 'dev') + '.cfg')

    from .models import db
    db.init_app(app)

    Mail(app)
    SSLify(app, permanent=True)

    # register blueprints

    return app
