from http import HTTPStatus
from flask import Flask, jsonify, request
from uuid import uuid4

cities_storage = {
    "e594e65ae5f7441f89d8e9acdc378a73": {
        "uid": "e594e65ae5f7441f89d8e9acdc378a73",
        "cityname": "Moscow",
    },
    "338623dad24c45389620400506ffa707": {
        "uid": "338623dad24c45389620400506ffa707",
        "cityname": "Berlin",
    },
    "2d6fccc02c764d1ab4047adee0858f50": {
        "uid": "2d6fccc02c764d1ab4047adee0858f50",
        "cityname": "Prague",
    },
    "039016d11cb34244bbd8cf434f27ca18": {
        "uid": "039016d11cb34244bbd8cf434f27ca18",
        "cityname": "London",
    },
    "0e251e309bee4137b54c982a7fae533f": {
        "uid": "0e251e309bee4137b54c982a7fae533f",
        "cityname": "Paris",
    },
}


def city_validation(city):
    cityname = city['cityname']
    print(cityname)
    if not cityname:
        return
    
    if not cityname.isalpha():
        return

    # TODO: check city with "-" like "Петропавловск-камчатский"

    city['cityname'] = cityname.capitalize()
    return city


app = Flask(__name__)


@app.get('/api/cities/')
def get_cities():
    cities = [city for city in cities_storage.values()]
    return jsonify(cities)


@app.get('/api/cities/<uid>')
def get_by_id(uid):
    city = cities_storage.get(uid)
    if not city:
        return {'message': 'city not found'}, HTTPStatus.NOT_FOUND

    return city


@app.post('/api/cities/')
def add_city():
    city = request.json
    valid_city = city_validation(city)
    if not valid_city:
        return {'message': 'incorrect input'}, HTTPStatus.BAD_REQUEST

    city['uid'] = uuid4().hex
    cities_storage[city['uid']] = valid_city
    return city, HTTPStatus.CREATED


@app.put('/api/cities/<uid>')
def update_city(uid):
    if uid not in cities_storage:
        return {'message': 'city not found'}, HTTPStatus.NOT_FOUND
    
    city = request.json
    valid_city = city_validation(city)
    if not valid_city:
        return {'message': 'incorrect input'}, HTTPStatus.BAD_REQUEST

    cities_storage[uid] = valid_city
    return city, HTTPStatus.OK


@app.delete('/api/cities/<uid>')
def delete_city(uid):
    if uid not in cities_storage:
        return {'message': 'city not found'}, HTTPStatus.NOT_FOUND

    cities_storage.pop(uid)
    return {}, HTTPStatus.NO_CONTENT
    