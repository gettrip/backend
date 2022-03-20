from sqlalchemy.exc import IntegrityError

from backend.db import db_session
from backend.errors import ConflictError, NotFoundError
from backend.models import Travel


class TravelRepo:
    name = 'travel'

    def get_all(self) -> list[Travel]:
        return Travel.query.all()

    def get_by_id(self, uid: int) -> Travel:
        travel = Travel.query.filter(Travel.uid == uid).first()
        if not travel:
            raise NotFoundError(self.name)

        return travel

    def check_unique(self, user_uid, city_uid, name):
        user_uid_list = Travel.query.filter(Travel.user_uid == user_uid)
        city_uid_list = user_uid_list.filter(Travel.city_uid == city_uid)
        travel_exist = city_uid_list.filter(Travel.name == name).first()
        if travel_exist:
            raise ConflictError(self.name)

    def add(self, name: str, city_uid: int, user_uid: int) -> Travel:
        self.check_unique(user_uid, city_uid, name)

        try:
            travel = Travel(name=name, city_uid=city_uid, user_uid=user_uid)
            db_session.add(travel)
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name)

        return travel

    def update(self, name: str, city_uid: int, uid: int, user_uid: int) -> Travel:
        travel = Travel.query.filter(Travel.uid == uid).first()
        if not travel:
            raise NotFoundError(self.name)

        self.check_unique(user_uid, city_uid, name)

        try:
            travel.name = name
            travel.city_uid = city_uid
            travel.user_uid = user_uid
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name)

        return travel

    def delete(self, uid: int) -> None:
        travel = Travel.query.filter(Travel.uid == uid).first()
        db_session.delete(travel)
        db_session.commit()
