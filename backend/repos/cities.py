import flask
from sqlalchemy.exc import IntegrityError

from backend.db import Base, get_db
from backend.errors import ConflictError, NotFoundError
from backend.models import City


class CityRepo:
    name = 'city'

    def get_all(self) -> list[City]:
        db_session = get_db(flask.current_app.config['db']['url'])
        Base.query = db_session.query_property()
        return City.query.all()

    def get_by_id(self, uid: int) -> City:
        db_session = get_db(flask.current_app.config['db']['url'])
        Base.query = db_session.query_property()
        city = City.query.filter(City.uid == uid).first()
        if not city:
            raise NotFoundError(self.name)

        return city

    def add(self, name: str, image: str) -> City:
        db_session = get_db(flask.current_app.config['db']['url'])
        try:
            city = City(name=name, image=image)
            db_session.add(city)
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name)

        return city

    def update(self, name: str, uid: int, image: str) -> City:
        db_session = get_db(flask.current_app.config['db']['url'])
        Base.query = db_session.query_property()
        city = City.query.filter(City.uid == uid).first()
        if not city:
            raise NotFoundError(self.name)

        try:
            city.name = name
            city.image = image
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name)

        return city

    def delete(self, uid: int) -> None:
        db_session = get_db(flask.current_app.config['db']['url'])
        Base.query = db_session.query_property()
        city = City.query.filter(City.uid == uid).first()
        db_session.delete(city)
        db_session.commit()
