#!/usr/bin/python3
"""New views for City objects"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State
from models.city import City


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities_by_state_id(state_id):
    """Get method for retrieve all cities based on state_id"""
    for state in storage.all(State).values():
        if state.id == state_id:
            list_city = []
            for city in state.cities:
                list_city.append(city.to_dict())
            return jsonify(list_city)
    return abort(404)


@app_views.route('/cities/<city_id>', methods=['GET'],
                 strict_slashes=False)
def get_city_id(city_id):
    """Retrieves get method for a city with a given id"""
    for city in storage.all(City).values():
        if city.id == city_id:
            return jsonify(city.to_dict())
    return abort(404)


@app_views.route('/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_city(city_id):
    """ Method that deletes a city based on its ID. """
    for city in storage.all(City).values():
        if city.id == city_id:
            city.delete()
            storage.save()
            return jsonify({})
    return abort(404)


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def post_city_by_state_id(state_id):
    """ Method that create a new city based on state_id. """
    state = storage.get(State, state_id)
    if state is None:
        return abort(404)

    params = request.get_json()
    if params is None:
        return abort(400, "Not a JSON")
    if "name" not in params.keys():
        return abort(400, "Missing name")
    new = City(**params)
    new.save()
    return jsonify(new.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'],
                 strict_slashes=False)
def put_city(city_id):
    """Method that updates a city based on its id"""
    city = storage.get(City, city_id)
    if city is None:
        return abort(404)
    params = request.get_json()
    if params is None:
        return abort(400, "Not a JSON")
    for k, v in params.items():
        if k != 'id' and k != 'created_at' and k != 'updated_at':
            setattr(city, k, v)
    city.save()
    return jsonify(city.to_dict())
