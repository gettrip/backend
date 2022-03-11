from backend.models import City
from backend.errors import Conflict, NotFound
from backend.db import db_session
from sqlalchemy.exc import IntegrityError
from typing import Optional

class CityRepo:

    
    def get_all(self) -> list[City]:        
        return City.query.all()

    
    def get_by_id(self, uid: int) -> Optional[City]:
        city = City.query.filter(City.uid==uid).first()
        if not city:
            raise NotFound('city')

        return city

    
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
        if not city:
            raise NotFound('city')

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
