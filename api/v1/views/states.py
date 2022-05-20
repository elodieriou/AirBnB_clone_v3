#!/usr/bin/python3
"""This modules defines the view for State object to handles all default API
actions"""
from flask import jsonify, abort, request
from models.state import State
from models import storage
from api.v1.views import app_views


@app_views.route('/states', methods=['GET'],
                 strict_slashes=False)
def get_states():
    """Retrieves get method for all state"""
    list_state = []
    all_state = storage.all(State).values()
    for state in all_state:
        list_state.append(state.to_dict())
    return jsonify(list_state)


@app_views.route('/states/<state_id>', methods=['GET'],
                 strict_slashes=False)
def get_state_id(state_id):
    """Retrieves get method for a state with a given id"""
    for state in storage.all(State).values():
        if state.id == state_id:
            return jsonify(state.to_dict())
    abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """ Method that deletes a state based on its ID. """
    for state in storage.all(State).values():
        if state.id == state_id:
            state.delete()
            storage.save()
            return jsonify({})
    abort(404)


@app_views.route('/states', methods=['POST'],
                 strict_slashes=False)
def post_state():
    """ Method that create a new state. """
    try:
        params = request.get_json()
    except Exception:
        return abort(400, "Not a JSON")
    if "name" not in params.keys():
        return abort(400, "Missing name")
    n = params['name']
    new = State(name=n)
    new.save()
    return jsonify(new.to_dict()), 201


@app_views.route('states/<state_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    """ Method that update a state. """
    state = storage.get(State, state_id)
    if state is None:
        return abort(404)
    try:
        params = request.get_json()
    except Exception:
        return abort(400, "Not a JSON")
    for k, v in params.items():
        if k != 'id' and k != 'created_at' and k != 'updated_at':
            setattr(state, k, v)
    state.save()
    return jsonify(state.to_dict())