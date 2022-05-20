#!/usr/bin/python3
"""This modules defines the view for User object to handles all default API
actions"""
from flask import jsonify, abort, request
from models.user import User
from models import storage
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'],
                 strict_slashes=False)
def get_users():
    """Retrieves get method for all users"""
    list_users = []
    all_a = storage.all(User).values()
    for user in all_a:
        list_users.append(user.to_dict())
    return jsonify(list_users)


@app_views.route('/users/<user_id>', methods=['GET'],
                 strict_slashes=False)
def get_user_id(user_id):
    """Retrieves get method for a user with a given id"""
    user = storage.get(User, user_id)
    if user is None:
        return abort(404)
    return jsonify(user.to_dict())


@app_views.route('/user/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id):
    """ Method that deletes an user based on its ID. """
    user = storage.get(User, user_id)
    if user is None:
        return abort(404)
    user.delete()
    storage.save()
    return jsonify({})


@app_views.route('/users', methods=['POST'],
                 strict_slashes=False)
def post_user():
    """ Method that create a new user. """
    params = request.get_json()
    if params is None:
        abort(400, "Not a JSON")
    if params.get("email") is None:
        abort(400, "Missing email")
    if params.get("password") is None:
        abort(400, "Missing password")
    new = User(**params)
    new.save()
    return jsonify(new.to_dict()), 201


@app_views.route('users/<user_id>',
                 methods=['PUT'], strict_slashes=False)
def put_user(user_id):
    """ Method that update an user. """
    user = storage.get(User, user_id)
    if user is None:
        return abort(404)
    params = request.get_json()
    if params is None:
        return abort(400, "Not a JSON")
    for k, v in params.items():
        if k != 'id' and k != 'created_at'
        and k != 'updated_at' and k != "email":
            setattr(user, k, v)
    user.save()
    return jsonify(user.to_dict())
