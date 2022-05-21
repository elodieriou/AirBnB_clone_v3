#!/usr/bin/python3
"""This modules defines the view for Place object to handles all default API
actions"""
from flask import jsonify, abort, request
from models.place import Place
from models.city import City
from models.user import User
from models import storage
from api.v1.views import app_views


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def get_places(city_id):
    """Retrieves get method for all places"""
    for city in storage.all(City).values():
        if city.id == city_id:
            list_places = []
            for place in city.places:
                list_places.append(place.to_dict())
            return jsonify(list_places)
    return abort(404)


@app_views.route('/places/<place_id>', methods=['GET'],
                 strict_slashes=False)
def get_place(place_id):
    """Retrieves get method for a place with a given id"""
    place = storage.get(Place, place_id)
    if place is None:
        return abort(404)
    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    """ Method that deletes a place based on its ID. """
    place = storage.get(Place, place_id)
    if place is None:
        return abort(404)
    place.delete()
    storage.save()
    return jsonify({})


@app_views.route('/cities/<city_id>/places', methods=['POST'],
                 strict_slashes=False)
def post_place(city_id):
    """ Method that create a new place. """
    city = storage.get(City, city_id)
    if city is None:
        return abort(404)
    params = request.get_json()
    if params is None:
        abort(400, "Not a JSON")
    if params.get("user_id") is None:
        abort(400, "Missing user_id")
    user = storage.get(User, params['user_id'])
    if user is None:
        return abort(404)
    if params.get("name") is None:
        abort(400, "Missing name")
    new = Place(**params)
    new.save()
    return jsonify(new.to_dict()), 201


@app_views.route('/places/<place_id>',
                 methods=['PUT'], strict_slashes=False)
def put_place(place_id):
    """ Method that update an place. """
    place = storage.get(Place, place_id)
    if place is None:
        return abort(404)
    params = request.get_json()
    if params is None:
        return abort(400, "Not a JSON")
    li = ["id", "created_at", "updated_at", "user_id"]
    for k, v in params.items():
        if k not in li:
            setattr(place, k, v)
    place.save()
    return jsonify(place.to_dict())
