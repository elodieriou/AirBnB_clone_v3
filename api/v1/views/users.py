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


"""@app_views.route('/users', methods=['POST'],
                 strict_slashes=False)
def post_user():
    "" Method that create a new user. ""
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
    "" Method that update an user. ""
    user = storage.get(User, user_id)
    if user is None:
        return abort(404)
    params = request.get_json()
    if params is None:
        return abort(400, "Not a JSON")
    li = ["id", "created_at", "updated_at", "email"]
    for k, v in params.items():
        if k not in li:
            setattr(user, k, v)
    user.save()
    return jsonify(user.to_dict())
"""
@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """create a new user"""
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'email' not in request.get_json():
        return make_response(jsonify({'error': 'Missing email'}), 400)
    if 'password' not in request.get_json():
        return make_response(jsonify({'error': 'Missing password'}), 400)
    user = User(**request.get_json())
    user.save()
    return make_response(jsonify(user.to_dict()), 201)


@app_views.route('/users/<string:user_id>', methods=['PUT'],
                 strict_slashes=False)
def put_user(user_id):
    """update a user"""
    user = storage.get("User", user_id)
    if user is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, val in request.get_json().items():
        if attr not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, attr, val)
    user.save()
    return jsonify(user.to_dict())
