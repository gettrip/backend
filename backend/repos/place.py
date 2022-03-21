from sqlalchemy.exc import IntegrityError

from backend.db import db_session
from backend.errors import ConflictError, NotFoundError
from backend.models import Place


class PlaceRepo:
    name = 'place'

    def get_all(self) -> list[Place]:
        return Place.query.all()

    def get_by_id(self, uid: int) -> Place:
        place = Place.query.filter(Place.uid == uid).first()
        if not place:
            raise NotFoundError(self.name)

        return place

    def add(self, name: str, city_id: int) -> Place:
        try:
            place = Place(name=name, city_id=city_id)
            db_session.add(place)
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name)

        return place

    def update(self, name: str, uid: int, city_id: int) -> Place:
        place = Place.query.filter(Place.uid == uid).first()
        if not place:
            raise NotFoundError(self.name)

        try:
            place.name = name
            place.city_id = city_id
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name)

        return place

    def delete(self, uid: int) -> None:
        place = Place.query.filter(Place.uid == uid).first()
        db_session.delete(place)
        db_session.commit()
