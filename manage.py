# -*- coding: utf-8 -*-

import os
import logging

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from backend.main import create_app
from backend.models import db


logger = logging.getLogger('backend-manage')
logger.setLevel(logging.DEBUG)

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db, os.path.abspath(os.path.join(os.path.dirname(__file__), 'backend', 'alembic')))
manager.add_command('db', MigrateCommand)


@manager.command
def runserver():
    '''Overrides the default runserver command'''
    app = create_app()
    app.run()


@manager.shell
def shell_context():
    '''Populates the shell with default imports. Add common imports here.'''
    return {
        'app': app,
        'db': db,
    }


if __name__ == '__main__':
    manager.run()
