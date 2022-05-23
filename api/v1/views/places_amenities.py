#!/usr/bin/python3
"""This modules defines the view for Amenity object to handles all default API
actions"""
from flask import jsonify, abort, request
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity
from models import storage
from api.v1.views import app_views


@app_views.route('/places/<place_id>/amenities', methods=['GET'],
                 strict_slashes=False)
def get_amenities(place_id):
    """Retrieves get method for all amenities"""
    for place in storage.all(Place).values():
        if place.id == place_id:
            list_am = []
            for a in place.amenities:
                list_am.append(a.to_dict())
            return jsonify(list_am)
    return abort(404)


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_place(place_id, amenity_id):
    """ Method that deletes a Amenity object to a place. """
    place = storage.get(Place, place_id)
    if place is None:
        return abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return abort(404)
    if amenity not in place.amenities:
        return abort(404)
    amenity.delete()
    storage.save()
    return jsonify({})


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['POST'], strict_slashes=False)
def post_amenity(place_id, amenity_id):
    """ Method that links a Amenity object to a Place. """
    place = storage.get(Place, place_id)
    if place is None:
        return abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return abort(404)
    if amenity in place.amenities:
        return amenity
    place.amenities.append(amenity)
    return (amenity), 201
