import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'alembic',
    'Flask',
    'Flask-Migrate',
    'Flask-Script',
    'Flask-SqlAlchemy',
    'Flask-SSLify',
    'Flask-Mail',
    'raven',
]

setup(
    name='backend',
    version='1.0',
    description='Flask Backend',
    long_description='Flask Backend for RESTfool APIs',
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='Peter Lada',
    author_email='peter@peterlada.com',
    url='https://github.org/peterlada/flask-backend',
    keywords='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=['nose', 'coverage'],
    namespace_packages=['backend'],
    test_suite="nose.collector",
    entry_points={
        'console_scripts': [
            'backend = manage:manager.run',
        ],
    },
)
