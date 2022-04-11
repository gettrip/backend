from sqlalchemy.exc import IntegrityError

from backend.db import db_session
from backend.errors import ConflictError, NotFoundError
from backend.models import City


class CityRepo:
    name = 'city'

    def get_all(self) -> list[City]:
        return City.query.all()

    def get_by_id(self, uid: int) -> City:
        city = City.query.filter(City.uid == uid).first()
        if not city:
            raise NotFoundError(self.name)

        return city

    def add(self, name: str, image: str) -> City:
        try:
            city = City(name=name, image=image)
            db_session.add(city)
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name)

        return city

    def update(self, name: str, uid: int, image: str) -> City:
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
        city = City.query.filter(City.uid == uid).first()
        db_session.delete(city)
        db_session.commit()
