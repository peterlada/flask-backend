from flask import current_app as app


@app.route('/')
def hi():
    return 'Hello'
