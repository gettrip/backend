from backend.models import City
from backend.errors import Conflict
from backend.db import db_session
from sqlalchemy.exc import IntegrityError


class CityRepo:

    
    def get_all(self) -> list[City]:        
        return City.query.all()

    
    def get_by_id(self, uid: int) -> City:
        return City.query.filter(City.uid==uid).first()

    
    def add(self, name: str) -> City:
        try:            
            city = City(name=name)
            db_session.add(city)
            db_session.commit()                       
        except IntegrityError:
            raise Conflict('city')
        
        return city


    def update(self, name: str, uid: int) -> City:
        city = City.query.filter(City.uid==uid).first()        
        try:
            city.name = name
            db_session.commit()                        
        except IntegrityError:
            raise Conflict('city')   
        
        return city

    
    def delete(self, uid: int) -> None:
        city = City.query.filter(City.uid==uid).first()        
        db_session.delete(city)
        db_session.commit()
