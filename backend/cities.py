import logging
import sqlalchemy.exc

from http import HTTPStatus
from flask import jsonify, request, Blueprint
from uuid import uuid4
from backend.db import db_session
from backend.models import City


logger = logging.getLogger(__name__)

cities_storage = {
    "e594e65ae5f7441f89d8e9acdc378a73": {
        "uid": "e594e65ae5f7441f89d8e9acdc378a73",
        "name": "Moscow",
    },
    "338623dad24c45389620400506ffa707": {
        "uid": "338623dad24c45389620400506ffa707",
        "name": "Berlin",
    },
    "2d6fccc02c764d1ab4047adee0858f50": {
        "uid": "2d6fccc02c764d1ab4047adee0858f50",
        "name": "Prague",
    },
    "039016d11cb34244bbd8cf434f27ca18": {
        "uid": "039016d11cb34244bbd8cf434f27ca18",
        "name": "London",
    },
    "0e251e309bee4137b54c982a7fae533f": {
        "uid": "0e251e309bee4137b54c982a7fae533f",
        "name": "Paris",
    },
}


cities = Blueprint('cities', __name__)


@cities.get('/')
def get_cities():
    cities = [city for city in cities_storage.values()]
    return jsonify(cities)


@cities.get('/<uid>')
def get_by_id(uid):
    city = cities_storage.get(uid)
    if not city:
        return {'message': 'city not found'}, HTTPStatus.NOT_FOUND

    return city


@cities.post('/')
def add_city():
    city = request.json
    city['uid'] = uuid4().hex     
    try:
        city_add = City(uid = city['uid'], name = city['name'])
        db_session.add(city_add)
        db_session.commit()
    except sqlalchemy.exc.IntegrityError:
        return {'message': 'city already exist'}, HTTPStatus.BAD_REQUEST

    return city, HTTPStatus.CREATED
   

@cities.put('/<uid>')
def update_city(uid):
    if uid not in cities_storage:
        return {'message': 'city not found'}, HTTPStatus.NOT_FOUND
    
    city = request.json
    valid_city = city_validation(city)
    if not valid_city:
        return {'message': 'incorrect input'}, HTTPStatus.BAD_REQUEST

    cities_storage[uid] = valid_city
    return city, HTTPStatus.OK


@cities.delete('/<uid>')
def delete_city(uid):
    if uid not in cities_storage:
        return {'message': 'city not found'}, HTTPStatus.NOT_FOUND

    cities_storage.pop(uid)
    return {}, HTTPStatus.NO_CONTENT
