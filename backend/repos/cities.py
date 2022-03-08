from backend.models import City
from backend.errors import Conflict
from backend.db import db_session
from sqlalchemy.exc import IntegrityError
from http import HTTPStatus


class CityRepo:

    
    def get_all(self):
        cities = [{'name': city.name, 'uid': city.uid} for city in City.query.all()]
        return cities

    
    def get_by_id(self, uid: int):
        city = City.query.filter(City.uid==uid).first()
        if not city:
            return {'message': 'city not found'}, HTTPStatus.NOT_FOUND
            # TODO: add "raise" instead "return" ones errors.py updated.

        return city

    
    def add(self, name: str):
        try:            
            city = City(name=name)
            db_session.add(city)
            db_session.commit()                       
        except IntegrityError:
            raise Conflict('city')
        
        return city


    def update(self, name: str, uid: int):
        city = City.query.filter(City.uid==uid).first()
        if not city:
            return {'message': 'city not found'}, HTTPStatus.NOT_FOUND    
            # TODO: add "raise" instead "return" ones errors.py updated.
    
        try:
            city.name = name
            db_session.commit()                        
        except IntegrityError:
            raise Conflict('city')   
        
        return city

    
    def delete(self, uid: int):
        city = City.query.filter(City.uid==uid).first()
        if not city:
            return {'message': 'city not found'}, HTTPStatus.NOT_FOUND
            # TODO: add "raise" instead "return" ones errors.py updated.

        db_session.delete(city)
        db_session.commit()
