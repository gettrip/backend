import logging
import werkzeug.exceptions

from http import HTTPStatus
from flask import jsonify, request, Blueprint
from uuid import uuid4
from backend.db import db_session
from backend.models import City
from pydantic import ValidationError
from backend.schemas import CitySchema


logger = logging.getLogger(__name__)

cities = Blueprint('cities', __name__)


@cities.get('/')
def get_cities():
    cities = [{'name': city.name, 'uid': city.uid} for city in City.query.all()]
    return jsonify(cities), HTTPStatus.OK


@cities.get('/<uid>')
def get_by_id(uid):
    city = City.query.filter(City.uid==uid).first()
    if not city:
        return {'message': 'city not found'}, HTTPStatus.NOT_FOUND

    return jsonify({'name': city.name, 'uid': city.uid}), HTTPStatus.OK


@cities.post('/')
def add_city():
    try:     
        payload = request.json
        payload['uid'] = uuid4().hex
        new_city = CitySchema(**payload)        
    except ValidationError as e:             
        return e.json(), HTTPStatus.BAD_REQUEST             
    except werkzeug.exceptions.BadRequest:
        return {"message": "data is incorrect"}, HTTPStatus.BAD_REQUEST

    city = City(uid=new_city.uid, name=new_city.name)
    db_session.add(city)
    db_session.commit()       

    
    return new_city.dict(), HTTPStatus.CREATED
   

@cities.put('/<uid>')
def update_city(uid):
    city = City.query.filter(City.uid==uid).first()
    if not city:
        return {'message': 'city not found'}, HTTPStatus.NOT_FOUND    
  
    try:
        new_name = request.json
    except werkzeug.exceptions.BadRequest:
        return {'message': 'incorrect input'}, HTTPStatus.BAD_REQUEST
    city.name = new_name['name']
    db_session.commit()    
    return new_name, HTTPStatus.OK


@cities.delete('/<uid>')
def delete_city(uid):
    city = City.query.filter(City.uid==uid).first()
    if not city:
        return {'message': 'city not found'}, HTTPStatus.NOT_FOUND

    db_session.delete(city)
    db_session.commit()
    return {}, HTTPStatus.NO_CONTENT
