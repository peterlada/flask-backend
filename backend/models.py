from flask.ext.sqlalchemy import SQLAlchemy
# no app object passed! Instead we use use db.init_app in the factory.
db = SQLAlchemy()

# create some models


class Example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(200), nullable=False)
