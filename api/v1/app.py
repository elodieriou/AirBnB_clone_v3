#!/usr/bin/python3
"""This module starts a Flask web application"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)

host = getenv('HBNB_API_HOST', '0.0.0.0')
port = getenv('HBNB_API_PORT', '5000')


@app.teardown_appcontext
def tear_down(exception):
    """The method remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
