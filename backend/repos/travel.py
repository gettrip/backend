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

    def add(self, name: str, city_id: int, user_id: int) -> Travel:
        try:
            travel = Travel(name=name, city_id=city_id, user_id=user_id)
            db_session.add(travel)
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name)

        return travel

    def update(self, name: str, city_id: int, uid: int, user_id: int) -> Travel:
        travel = Travel.query.filter(Travel.uid == uid).first()
        if not travel:
            raise NotFoundError(self.name)

        try:
            travel.name = name
            travel.city_id = city_id
            travel.user_id = user_id
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name)

        return travel

    def delete(self, uid: int) -> None:
        travel = Travel.query.filter(Travel.uid == uid).first()
        db_session.delete(travel)
        db_session.commit()
