import logging
import sqlalchemy.exc

from http import HTTPStatus
from flask import jsonify, request, Blueprint
from backend.errors import Conflict
from backend.db import db_session
from backend.models import City
from backend import schemas


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
        new_city = schemas.City(**payload)   
        city = City(name=new_city.name)
        db_session.add(city)
        db_session.commit()           
        new_city = schemas.City.from_orm(city)
    except sqlalchemy.exc.IntegrityError:
        raise Conflict('city')

    return new_city.dict(), HTTPStatus.CREATED
   

@cities.put('/<uid>')
def update_city(uid):
    city = City.query.filter(City.uid==uid).first()
    if not city:
        return {'message': 'city not found'}, HTTPStatus.NOT_FOUND    
  
    try:
        payload = request.json
        new_city = schemas.City(**payload)
        city.name = new_city.name
        db_session.commit()    
        new_city = schemas.City.from_orm(city)
    except sqlalchemy.exc.IntegrityError:
        raise Conflict('city')        

    return new_city.dict(), HTTPStatus.OK


@cities.delete('/<uid>')
def delete_city(uid):
    city = City.query.filter(City.uid==uid).first()
    if not city:
        return {'message': 'city not found'}, HTTPStatus.NOT_FOUND

    db_session.delete(city)
    db_session.commit()
    return {}, HTTPStatus.NO_CONTENT
