#!/usr/bin/python3
"""This modules defines the view for Place object to handles all default API
actions"""
from flask import jsonify, abort, request
from models.place import Place
from models.city import City
from models.user import User
from models.review import Review
from models import storage
from api.v1.views import app_views


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_reviews(place_id):
    """Retrieves get method for all reviews"""
    for place in storage.all(Place).values():
        if place.id == place_id:
            list_r = []
            for review in place.reviews:
                list_r.append(review.to_dict())
            return jsonify(list_r)
    return abort(404)


@app_views.route('/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_review(review_id):
    """Retrieves get method for a review with a given id"""
    review = storage.get(Review, review_id)
    if review is None:
        return abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id):
    """ Method that deletes a review based on its ID. """
    review = storage.get(Review, review_id)
    if review is None:
        return abort(404)
    review.delete()
    storage.save()
    return jsonify({})


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def post_review(place_id):
    """ Method that create a new review. """
    place = storage.get(Place, place_id)
    if place is None:
        return abort(404)
    params = request.get_json()
    if params is None:
        abort(400, "Not a JSON")
    if params.get("user_id") is None:
        abort(400, "Missing user_id")
    user = storage.get(User, params['user_id'])
    if user is None:
        return abort(404)
    if params.get("text") is None:
        abort(400, "Missing text")
    params['place_id'] = place_id
    new = Review(**params)
    new.save()
    return jsonify(new.to_dict()), 201


@app_views.route('/reviews/<review_id>',
                 methods=['PUT'], strict_slashes=False)
def put_review(review_id):
    """ Method that update a review. """
    review = storage.get(Review, review_id)
    if review is None:
        return abort(404)
    params = request.get_json()
    if params is None:
        return abort(400, "Not a JSON")
    li = ["id", "created_at", "updated_at", "user_id", "place_id"]
    for k, v in params.items():
        if k not in li:
            setattr(review, k, v)
    review.save()
    return jsonify(review.to_dict())
