#!/usr/bin/python3
"""Route to connect API"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """HBNB status"""
    return jsonify({'status': 'OK'})
