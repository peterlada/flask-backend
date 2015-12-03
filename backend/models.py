from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# create some models


class Example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, nullable=False)
