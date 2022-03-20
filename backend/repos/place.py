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

    def add(self, name: str, city_uid: int) -> Place:
        city_uid_list = Place.query.filter(Place.city_uid == city_uid)
        place_exist = city_uid_list.filter(Place.name == name).first()
        if place_exist:
            raise ConflictError(self.name)

        try:
            place = Place(name=name, city_uid=city_uid)
            db_session.add(place)
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name)

        return place

    def update(self, name: str, city_uid: int, uid: int) -> Place:
        place = Place.query.filter(Place.uid == uid).first()
        if not place:
            raise NotFoundError(self.name)

        city_uid_list = Place.query.filter(Place.city_uid == city_uid)
        place_exist = city_uid_list.filter(Place.name == name).first()
        if place_exist:
            raise ConflictError(self.name)

        try:
            place.name = name
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name)

        return place

    def delete(self, uid: int) -> None:
        place = Place.query.filter(Place.uid == uid).first()
        db_session.delete(place)
        db_session.commit()
