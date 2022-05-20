#!/usr/bin/python3
"""This modules defines the view for Amenity object to handles all default API
actions"""
from flask import jsonify, abort, request
from models.amenity import Amenity
from models import storage
from api.v1.views import app_views


@app_views.route('/amenities', methods=['GET'],
                 strict_slashes=False)
def get_amenities():
    """Retrieves get method for all amenities"""
    list_amenities = []
    all_a = storage.all(Amenity).values()
    for amenity in all_a:
        list_amenities.append(amenity.to_dict())
    return jsonify(list_amenities)


@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenity_id(amenity_id):
    """Retrieves get method for a amenity with a given id"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_amenity(amenity_id):
    """ Method that deletes an amenity based on its ID. """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return abort(404)
    amenity.delete()
    storage.save()
    return jsonify({})


@app_views.route('/amenities', methods=['POST'],
                 strict_slashes=False)
def post_amenity():
    """ Method that create a new amenity. """
    params = request.get_json()
    if params is None:
        abort(400, "Not a JSON")
    if params.get("name") is None:
        abort(400, "Missing name")
    new = Amenity(**params)
    new.save()
    return jsonify(new.to_dict()), 201


@app_views.route('amenities/<amenity_id>',
                 methods=['PUT'], strict_slashes=False)
def put_amenity(amenity_id):
    """ Method that update an amenity. """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return abort(404)
    params = request.get_json()
    if params is None:
        return abort(400, "Not a JSON")
    for k, v in params.items():
        if k != 'id' and k != 'created_at' and k != 'updated_at':
            setattr(amenity, k, v)
    amenity.save()
    return jsonify(amenity.to_dict())
